import tweepy
import csv
import re
from textblob import TextBlob

#  These four keys are used to access the twitter api and also termed as consumer api keys and the access tokens
consumer_key='kPlWivApbRigx0T6ZGtSV2Gxu'
consumer_secret='WhUd5MPaTkdZFY0kh4uryMGhRhQKtwtAMvKJTEGtJYAMvrgWLv'
access_token='1044608872391028738-O11jab6VBg0Z4ENogCbK0jqov8iiLa'
access_secret='bkCoy0mCTuXye9qsTOpN87tZa1wDRmKCGwRKRGd59pYff'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret) # It authenticates the user's identity

auth.set_access_token(access_token,access_secret)

 # setting a variable to use tweepy
api=tweepy.API(auth,wait_on_rate_limit=True)

#open the file with 1000 tweets and it works as input file
csv_3 = open('sentiment3.csv','r')
csv_3Reader = csv.DictReader(csv_3)

# Declare the column names which are required in output file
fieldnames=['Tweet','Sentiment','SentimentScore']

csvNew = open('file4.csv','w',encoding='utf-8')
csvNewWriter = csv.DictWriter(csvNew,fieldnames=fieldnames)

csvNewWriter.writeheader() # Column names in csv file



tweet_text=[]

for row in csv_3Reader:

    tweet_text = row['Tweet'].split()

    for i in range(len(tweet_text)):
# removing un-necessary particles of the tweet in order to increase the efficiency of program
        if(tweet_text[i].find('@') >= 0 or tweet_text[i].find('&amp') >= 0 or tweet_text[i].find('https') >= 0):
            tweet_text[i] = "  "


# Removing the white spaces and emojis to improve the efficiency
    text = []
    #Removes the redundant white spaces
    text = re.sub(r"\s+", "",str(tweet_text))
    text1 = text
    text = []
    # Allows only alphabets
    text = re.sub('[^A-Za-z]+',' ',str(text1))
    text1 = []
    #Removes the single character and words having length 2-3
    text1 = re.sub(r'\b\w{1,3}\b',' ', str(text))
    text = []
    # Removes redundant spaces
    text = re.sub(' +', ' ',str(text1))


#Finding the sentiment score and bifurcating them into 3 categories
    sentiment_analysis = TextBlob(text)
    score = sentiment_analysis.sentiment.polarity
    if(score > 0.0):
        str1 = "Positive"

    elif(score < 0.0):
        str1 = "Negative"

    else:
        str1 = "Neutral"
#Adding all the data in final output csv file
    csvNewWriter.writerow({"Tweet" : row['Tweet'],"Sentiment" : str1 , "SentimentScore" : score})

csvNew.close()
