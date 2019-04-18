#!/usr/bin/python
# -*- coding: utf-8 -*-
from google.cloud import language
from tqdm import tqdm # This is an awesome package for tracking for loops
import pandas as pd
import json
import tweepy
import csv
import pandas as pd
import re

bigjson = []
info = {}

def store_info(tweet):
    info['Tweet'] = tweet
    bigjson.append(info.copy())

def gc_sentiment(text):  
       
    path = "C:/Users/iagboola/Documents/NLP/ADEOLA-NPL-48d51db0789c.json" #FULL path to your service account key
    client = language.LanguageServiceClient.from_service_account_json(path)
    document = language.types.Document(
            content=text,
            type=language.enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    return score, magnitude

# Twitter API credentials

# Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
 
# Create the api endpoint

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
tweets = []
parsed_tweet = []
# Mention the maximum number of tweets that you want to be extracted.

maximum_number_of_tweets_to_be_extracted = \
int(input('Enter the number of tweets that you want to extract- '))

# Mention the hashtag that you want to look out for

hashtag = input('Enter the hashtag you want to scrape- ')

for tweet in tweepy.Cursor(api.search, q='#' + hashtag, result_type="mixed", tweet_mode ='extended',lang ='en', rpp=100).items(maximum_number_of_tweets_to_be_extracted): 
    parsed_tweet.append(tweet.full_text.encode('utf-8'))

    #print(parsed_tweet)


#print(tweets)
    
for item in parsed_tweet:
    x =  ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z\t\n])|(\w+:\/\/\S+)"," ",  str(item)).split())
    y =  ' '.join(re.sub("^b|x\w*\d*"," ",  str(x)).split())
    if y not in tweets:
        tweets.append(y)

for i in tweets:
    store_info(i)
    with open('tweets_with_hashtag_' + hashtag + '.txt', 'a') as \
    the_file:
        the_file.write( str(i) + '\n')

#print(bigjson)

print ('Extracted ' + str(maximum_number_of_tweets_to_be_extracted) \
+ ' tweets with hashtag #' + hashtag)



gc_results = [gc_sentiment(row['Tweet']) for row in tqdm(bigjson, ncols = 1000)]
#print(gc_results) 
gc_score, gc_magnitude = zip(*gc_results) # Unpacking the result into 2 lists
gc = list(zip((row['Tweet'] for row in bigjson), gc_score, gc_magnitude))
columns = ['Tweet','Score', 'Magnitude']
gc_df = pd.DataFrame(gc, columns = columns)

gc_df.to_csv('T_SA.csv',sep=',', encoding='utf-8')


