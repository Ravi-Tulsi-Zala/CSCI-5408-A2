#Necessary imports for csv to json conversion, elasticsearch bulkapis of Helpers 

import json
import csv
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

#Connection to Elasticsearch cluster , URL : ['https://username:password@url']

es = Elasticsearch(['https://admin:WQFKIEFSGVQBSZLE@portal-ssl1268-23.bmix-dal-yp-52259031-bb42-47f3-8f8c-abe1251c2ec8.2735667706.composedb.com:58050'])

#Health() method will return the connection information and Ping method will return True if connection is successfull 

print(es.cluster.health(),es.ping()) 



#Create() method will create index 

es.indices.create(index="tweets",ignore=400)

#get_alias() method will return all the indices I created

print(es.indices.get_alias("*"))


csv_file = open('file4.csv', 'r')

#w+ mode is used for both reading and writing , The file is created if it does not exist, otherwise it is truncated.
json_file = open('file16.json', 'w+') #w+ mode is used for both reading and writing 

fields = ("Tweet","Sentiment","SentimentScore")
csv_reader = csv.DictReader(csv_file, fields)

#Iterate through csv file row by row
for row in csv_reader:

    json.dump(row, json_file)   #Serializing data for translation row of csvfile to jsonfile
    json_file.write('\n')


json_file.close()

#This function is used to insert data into index mentioned above (here "tweets")

def bulk_insert():

    for line in open('file16.json', 'r'):
        
        tweet_data = json.loads(line) #A single line is a row of tweet,sentiment,score... Which is loaded in tweet_data
        
        
        yield{
                "_index": "tweets",
                "_type": "document",
                "_source":{
                           "Tweet":tweet_data['Tweet'],
                           "Sentiment":tweet_data['Sentiment'],
                            "Sentiment_Score":tweet_data['SentimentScore']}  # Mapping of keys to values for inserting the data.
        }


bulk(es, bulk_insert()) #bulk() is used for inserting the data into particular index

json_file.close()   
    
    


#Searching the tweets which are Neutral

result = es.search(index="tweets", body={"query": {"match":{"Sentiment":"Neutral"}}})
print("Got %d Hits:" % result['hits']['total'])



for hit in result['hits']['hits']:
    print(hit["_source"])





