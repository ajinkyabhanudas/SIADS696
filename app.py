import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

import datetime
import glob
import json
import re
from itertools import groupby

import nltk
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
import pickle

import warnings
warnings.simplefilter(action='ignore')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler
from sklearn.preprocessing import FunctionTransformer, PolynomialFeatures, OneHotEncoder

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from sklearn.ensemble import RandomForestRegressor, HistGradientBoostingRegressor

import gensim.downloader

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


def create_train_dataset(df, featureset=None, d=5):
    df["publishedAt"] = pd.to_datetime(df.publishedAt)
    df['publishedDayNum'] = df.publishedAt.apply(lambda x: x.timetuple().tm_yday)
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
        axis=1)
    return train_X


def creator_details():

    featureset = ["title", "duration", "publishedAt", "definition", "topicLabel"]

    data_dict = {}

    data_dict['title'] = st.text_input(
        'What is the title of the video',
    )
    data_dict['duration'] = st.number_input(
        'How many seconds long is your video?',
        min_value=1,
    )
    hd = st.radio(
        "Does the video support hd quality?",
        ('Yes', 'No'),
    )
    if hd == "Yes":
        data_dict['definition'] = "hd"
    else:
        data_dict['definition'] = "sd"

    data_dict['publishedAt'] = st.date_input(
        "When do you plan on uploading the video",
        min_value=datetime.datetime.now(),
    )

    available_topics_list = ("comedy", "cooking", "educational",
                             "fitness", "history", "music",
                             "news", "science", "travel",
                             "yoga")

    data_dict['topicLabel'] = st.radio(
        'What is the primary topic of your video?',
        available_topics_list)

    return data_dict


if __name__ == '__main__':

    st.header("Youtube Video Views Prediction")

    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False

    new_creator = st.radio(
        "Are you a new content creator?",
        ('Yes', 'No'),
    )

    if new_creator == 'Yes':
        st.write("Let's get started then...")

        df = pd.DataFrame(creator_details(), index=[0])

        if not df.empty:
            st.write("This is what the model will use to make its prediction:")
            st.dataframe(df)

        filename = "model.sav"
        model = pickle.load(open(filename, 'rb'))
        if st.button('Predict'):
            glove_wv = gensim.downloader.load('glove-wiki-gigaword-50')

            nltk.download('punkt')
            nltk.download('stopwords')

            pred = model.predict(df)

            topic_stats = pd.read_csv("cat_stats.csv").set_index('topicLabel')

            topic = df.topicLabel.values[0]
            row = topic_stats.loc[topic]
            pt = pd.DataFrame([[row.loc['50%'], 'median'], [max(0,[row.loc['50%']*pred][0][0]), 'prediction']])
            print(pt)
            fig = px.bar(pt, x=1, y=0)

            st.plotly_chart(fig, use_container_width=True)

    else:
        st.write("Phase 2 Coming soon....")