import datetime
import pandas as pd
import streamlit as st


def creator_details():

    feature_set = ['title', 'topicCategories', 'definition', 'publishedDayNum', 'duration_secs']## fetch from eda notebook

    data_dict = {}

    data_dict['title'] = st.text_input(
        'What is the title of the video',
    )
    data_dict['duration_secs'] = st.number_input(
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

    available_topics_list = ["food", "knowledge", "music", "other"] ###load these from the preproc nb

    data_dict['topicCategories'] = []
    data_dict['topicCategories'].append(st.multiselect(
        'What topics does your video cover?',
        available_topics_list,
        available_topics_list[-1],
    ))

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

        df = pd.DataFrame(creator_details())
        if not df.empty:
            st.write("This is what the model will use to make its prediction:")
            st.dataframe(df)

    else:
        st.write("Coming soon....")