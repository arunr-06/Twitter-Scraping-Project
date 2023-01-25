import pandas as pd
import numpy as np
import seaborn as sns
import snscrape.modules.twitter as sntwitter
import streamlit as st
import time

st.markdown('# Twitter Analytics')

if 'a_counter' not in st.session_state:
    st.session_state['a_counter'] = 0

input_data = st.text_input('Enter the #hashtag')

from_date = st.date_input(label = 'From')
to_date = st.date_input(label = 'Until')
tweet_count = st.slider('No of Tweets', min_value=0, max_value=1000,step=10)

button = st.button('Display')

if button:
    'Fetching the data...'
    
    st.session_state['a_counter'] += 1
    a = sntwitter.TwitterHashtagScraper(f'#{input_data} since:{from_date} until:{to_date}').get_items()
    tweets_container = []
    for i,tweet in enumerate(a):
        if i>tweet_count:
            break
        tweets_container.append([tweet.date, tweet.id, tweet.content, tweet.url, 
        tweet.likeCount, tweet.replyCount, tweet.retweetCount, 
        tweet.lang, tweet.source])
        tweets_df = pd.DataFrame(tweets_container, columns = ['Date','ID','Content','URL',
                                                     'No of likes','No of replies','No of retweet',
                                                     'Language','Source'])
    st.dataframe(tweets_df)

    '...and we\'re done!'