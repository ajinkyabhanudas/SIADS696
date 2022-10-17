import datetime
import enum
import glob
import json
import os
import re
from itertools import groupby

from gensim.models import Word2Vec
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import numpy as np
import pandas as pd

import warnings

warnings.simplefilter(action='ignore')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.decomposition import PCA
import pickle

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer

from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.dummy import DummyRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import PolynomialFeatures

from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
from sklearn.model_selection import GridSearchCV

import gensim.downloader

glove_wv = gensim.downloader.load('glove-wiki-gigaword-50')

nltk.download('punkt')
nltk.download('stopwords')

rootdir = 'data'
feature_list = ['publishedAt', 'title', 'channelId', 'description',
                'channelTitle', 'tags', 'categoryId', 'viewCount',
                'likeCount', 'favoriteCount', 'commentCount', 'duration',
                'definition', 'contentRating', 'topicCategories', 'topicLabel']

ov_dict_list = []
ov_temp_dict = {}

dict_list = []
temp_dict = {}

for path in glob.glob(f'./{rootdir}/*/*'):
    try:
        with open(path, "r") as read_file:
            data = json.load(read_file)
        for channel_id in data.keys():
            ov_temp_dict = data[channel_id]["channel_statistics"]
            channel_name = list(data[channel_id]["video_data"].keys())[0]
            ov_temp_dict["channelName"] = data[channel_id]["video_data"][channel_name]["channelTitle"]
            ov_dict_list.append(ov_temp_dict)

            for video_info in data[channel_id]["video_data"].values():
                temp_dict = video_info
                temp_dict["topicLabel"] = path.split('/')[2]
                dict_list.append(temp_dict)
    except:
        pass

overall_stats_raw_df = pd.DataFrame(ov_dict_list)
overall_stats_raw_df.drop("hiddenSubscriberCount", axis=1, inplace=True)

raw_df = pd.DataFrame(dict_list)
raw_df = raw_df[feature_list]


def duration_split(duration):
    try:
        for _, v in groupby(duration, str.isalpha):
            yield ''.join(v)
    except:
        yield np.nan


def duration_2_secs(duration, duration_split=duration_split):
    temp = 0
    for i, val in enumerate(duration_split(duration)):

        if len(str(duration)) <= 8:
            if i == 1 and not val.isalpha():
                temp += float(val) * 60

            if i == 3 and not val.isalpha():
                temp += float(val)
        else:
            if i == 1 and not val.isalpha():
                temp += float(val) * 60 * 60

            if i == 3 and not val.isalpha():
                temp += float(val) * 60

            if i == 5 and not val.isalpha():
                temp += float(val)

    return (temp)


def topic_extract(links_list):
    topics_list = []
    try:
        for link in links_list:
            topics_list.append(link.split("/")[-1].lower())

        return (topics_list)
    except:
        pass


def gen_word_vec(df_text_list, wordvec):
    word_vector = []
    for token in df_text_list:
        token_considered = [t for t in token if t.isalpha]
        token_vocab = [i for i in token_considered if i in wordvec.key_to_index]
        if len(token_vocab) > 0:
            word_vector.append(np.mean(wordvec[token_vocab], axis=0))
        else:
            word_vector.append(np.zeros(wordvec.vector_size))
    word_vector = np.array(word_vector)
    try:
        return word_vector[0]
    except:
        return np.zeros(50)


def text_prep(val):
    '''the goal is to replace the hypertexts in the
    in any field to redundant names as vectorizing
    them could be misleading and also leak data'''

    val = str(val).lower()
    process_desc = re.sub(r'http[s]*:.*\w', 'url', val)
    process_desc = re.sub('[^a-zA-Z]', ' ', process_desc)
    process_desc = re.sub(r'\s+', ' ', process_desc)

    process_desc = nltk.sent_tokenize(process_desc)
    if not process_desc:
        process_desc = [nltk.word_tokenize(word) for word in process_desc]
    else:
        process_desc = [nltk.word_tokenize(word) for word in process_desc][0]

    word_list = [word for word in process_desc if word not in stopwords.words('english')]

    return word_list


def create_target(df):
    df["publishedAt"] = pd.to_datetime(df.publishedAt)
    df['publishedDayDelta'] = (datetime.datetime.now() - df.publishedAt.dt.tz_localize(None)).dt.days
    df["viewCount"] = df.viewCount.astype(float)
    df["avg_viewCount"] = df["viewCount"] / df['publishedDayDelta']
    df['topicLabel'] = df.topicLabel.str.lower()
    df['score'] = df["avg_viewCount"] / df.topicLabel.map(dict(df.groupby('topicLabel').avg_viewCount.agg('median')))

    return df['score']


def create_train_dataset(df, featureset=None, d=4):
    df["publishedAt"] = pd.to_datetime(df.publishedAt)
    df['publishedDayNum'] = df.publishedAt.apply(lambda x: x.timetuple().tm_yday)
    if df['duration'].dtype == 'O':
        df['duration_secs'] = df.duration.apply(duration_2_secs)
    else:
        df['duration_secs'] = df.duration.astype(int)
    df['topicLabel'] = df.topicLabel.str.lower()
    df['title'] = df.title.apply(text_prep)
    df['len_title'] = df.title.apply(lambda x: len(x))
    df['log_duration_secs'] = np.log(df.duration_secs + 1)
    df.loc[df['topicLabel'] == 'fitness_workout', 'topicLabel'] = 'fitness'

    df['vec_title'] = df.title.apply(gen_word_vec, wordvec=glove_wv)
    titles = df.vec_title.apply(pd.Series).rename(columns={i - 1: "title_" + str(i) for i in range(1, 51)})

    train_X = pd.concat(
        [df[['publishedDayNum', 'log_duration_secs', 'len_title']], titles, df.definition, df.topicLabel],
        axis=1).values
    poly = PolynomialFeatures(d)
    trainX3 = poly.fit_transform(train_X[:, :3])
    trainX62 = train_X[:, 3:]

    x_poly_ip = np.concatenate((trainX62, trainX3), axis=1)
    return x_poly_ip


def cat_stats(df):
    df["publishedAt"] = pd.to_datetime(df.publishedAt)
    df['publishedDayNum'] = df.publishedAt.apply(lambda x: x.timetuple().tm_yday)
    df['publishedDayDelta'] = (datetime.datetime.now() - df.publishedAt.dt.tz_localize(None)).dt.days
    df["viewCount"] = df.viewCount.astype(float)
    df["avg_viewCount"] = df["viewCount"] / df['publishedDayDelta']
    df['topicLabel'] = df.topicLabel.str.lower()
    df.loc[df['topicLabel'] == 'fitness_workout', 'topicLabel'] = 'fitness'

    return (df.groupby('topicLabel').avg_viewCount.describe())


cat_stats(raw_df).to_csv("cat_stats.csv")
data_train, data_test = train_test_split(raw_df, test_size=0.20, random_state=42)

data_train = data_train.dropna()
data_test = data_test.dropna()

target = create_target(data_train)
test_target = create_target(data_test)

print("Data Preprocessing Started...")
lr_pipeline = Pipeline([('create_dataset', FunctionTransformer(create_train_dataset)),
          ('ohe', OneHotEncoder(handle_unknown='ignore')),
          ('scale',MaxAbsScaler()),
          ('lr', LinearRegression())])

print("Model Training Started...")
lr_pipeline.fit(data_train, target)

filename = 'model.sav'
pickle.dump(lr_pipeline, open(filename, 'wb'))
print("Model Has Been Saved...")