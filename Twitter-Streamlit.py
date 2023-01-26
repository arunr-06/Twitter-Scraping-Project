import pandas as pd
import numpy as np
import seaborn as sns
import snscrape.modules.twitter as sntwitter
import streamlit as st
from pymongo import MongoClient
import certifi

st.markdown('# Twitter Analytics')

if 'a_counter' not in st.session_state:
    st.session_state['a_counter'] = 0

input_data = st.text_input('Enter the #hashtag')

from_date = st.date_input(label='From')
to_date = st.date_input(label='Until')
tweet_count = st.slider('No of Tweets', min_value=0, max_value=10000, step=10)

button = st.button('Display')

if button:
    'Fetching the data...'
    st.session_state['a_counter'] += 1
    a = sntwitter.TwitterHashtagScraper(
        f'#{input_data} since:{from_date} until:{to_date}').get_items()
    tweets_container = []
    for i, tweet in enumerate(a):
        if i > tweet_count:
            break
        tweets_container.append([tweet.date, tweet.id, tweet.content, tweet.url,
                                 tweet.likeCount, tweet.replyCount, tweet.retweetCount,
                                 tweet.lang, tweet.source])
        tweets_df = pd.DataFrame(tweets_container, columns=['Date', 'ID', 'Content', 'URL',
                                                            'No of likes', 'No of replies', 'No of retweet',
                                                            'Language', 'Source'])
    st.dataframe(tweets_df)

    '...and we\'re done!'

    def convert_df_csv(df):
        return df.to_csv().encode('utf-8')

    def convert_df_json(df):
        return df.to_json()

    def post_mongo(df):
        ca = certifi.where()
        pym = MongoClient('mongodb://Guvi:guvidw34@ac-xaisubg-shard-00-00.5ztguao.mongodb.net:27017,ac-xaisubg-shard-00-01.5ztguao.mongodb.net:27017,ac-xaisubg-shard-00-02.5ztguao.mongodb.net:27017/?ssl=true&replicaSet=atlas-tjrj1s-shard-0&authSource=admin&retryWrites=true&w=majority', tlsCAFile=ca)
        pym1 = pym['Twitter_Scraping']
        pym2 = pym1['Collection4']
        df1 = df.to_dict('records')
        pym2.insert_many(df1)

    csv_file = convert_df_csv(tweets_df)
    json_file = convert_df_json(tweets_df)

    st.download_button(label="Download the data as CSV?",
                       data=csv_file, file_name='tweet_data.csv', mime='text/csv')
    st.download_button(label="Download the data as JSON?",
                       data=json_file, file_name='tweet_data.json')
    st.button('Post the data to MongoDB?', on_click=post_mongo(tweets_df))