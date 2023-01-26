# Scraping data from Twitter

## Programming language used: 
Python

## Python libraries used: 
snscrape,pandas, streamlit, pymongo, certifi

## Applications used: 
VSCode, MongoDB

## Project overview: 
To perform analysis on a Twitter trend/hashtag, the data is retrieved from Twitter using Python library snscrape and converted to a dataframe using pandas. The dataframe is posted to a web app built using streamlit. Streamlit will have the option for the user to input parameters(date, count) & fetch the required data from Twitter through Python. 

## User workflow:
* User opens the streamlit app

* Provides input - hashtag, date, count & clicks display

* Receives output of individual tweets - `date, ID, URL, content, username, reply count, retweet count, language, source, like count`

* User downloads the retrieved data as a CSV or JSON file

* Alternatively, the user posts the data to MongoDB

## Code walkthrough:
* The session state is initialized to 0 at the beginning of the code & increments after the user clicks on the display button, to ensure that the code doesn’t run from the beginning all over again.

* sntwitter - module from library snscrape - retrieves data for the defined dates from Twitter. An empty list is created, and the Twitter data is appended to it until the count indicated by the user is satisfied.

* The list is converted to a pandas dataframe & displayed on the app.

* User-defined functions are created for the following actions - downloading CSV file, downloading JSON file, posting to MongoDB. 

* Download buttons are added for downloading & a generic button is added to call for action MongoDB posting.

* Inside the MongoDB function, the following activities take place - establishing a connection with the MongoDB collections, converting the pandas dataframe to a list, posting the list to the MongoDB collection. Before running the MongoDB function, the following activities need to be done - importing the certificate and adding it to MongoClient syntax to prevent certificate error, and creating a collection in the MongoDB application. 

## Result:
User will be able to download the Twitter data in the required format for further analysis

<img src="https://github.com/arunr-06/Twitter-Scraping-Project/blob/main/Thumbsup.jpg" class="inline"/>