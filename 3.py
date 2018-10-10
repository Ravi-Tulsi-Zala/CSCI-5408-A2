import tweepy
import csv
import json

#  These four keys are used to access the twitter api and also termed as consumer api keys and the access tokens
consumer_key='kPlWivApbRigx0T6ZGtSV2Gxu'
consumer_secret='WhUd5MPaTkdZFY0kh4uryMGhRhQKtwtAMvKJTEGtJYAMvrgWLv'
access_token='1044608872391028738-O11jab6VBg0Z4ENogCbK0jqov8iiLa'
access_secret='bkCoy0mCTuXye9qsTOpN87tZa1wDRmKCGwRKRGd59pYff'


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)  # It authenticates the user's identity

auth.set_access_token(access_token,access_secret)

# setting a variable to use tweepy
api=tweepy.API(auth,wait_on_rate_limit=True)

#open the csv to write the tweets
csvFile = open('sentiment3.csv','w',encoding='utf-8')

query = input("Enter a keyword/Hashtag : ")

numberOfTweets = int(input("Enter the number of tweets : "))

# Declare the column names which are required in output file
fieldnames=['Tweet']

csvWriter=csv.DictWriter(csvFile,fieldnames=fieldnames)

csvWriter.writeheader()

#Cursor method of tweepy searches the given hashtag and total number of tweets
if numberOfTweets >= 1000:
    tweets = tweepy.Cursor(api.search, q=query).items(numberOfTweets) # to search the twitter and extract all the matching tweets
    for tweet in tweets:
# Writing the tweets into the csv file
        csvWriter.writerow({"Tweet" : tweet.text.encode('utf-8')})
else:
    print("Enter value greater than 1000")

csvFile.close()
