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

####input your credentials here
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#####Buhari
# Open/Create a file to append data
csvFile = open('buhari.csv', 'w')
#Use csv Writer
csvWriter = csv.writer(csvFile)

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

for tweet in tweepy.Cursor(api.search,q="#Buhari",count=10, lang="en", result_type="popular", tweet_mode="extended").items():
    #print(tweet.created_at, tweet.text.encode('utf-8'))
    #print(str(tweet.text.encode('utf-8'))) 

    matobj = re.compile(r"[']*[A-Za-z]*[,]*")

    fin = re.findall(matobj, tweet.text)
   
    
   
    #print(''.join(fin))

    store_info(' '.join(fin))


    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

print(bigjson)

gc_results = [gc_sentiment(row['Tweet']) for row in tqdm(bigjson, ncols = 100)]
#print(gc_results) 
gc_score, gc_magnitude = zip(*gc_results) # Unpacking the result into 2 lists
gc = list(zip((row['Tweet'] for row in bigjson), gc_score, gc_magnitude))
columns = ['Tweet', 'Score', 'Magnitude']
gc_df = pd.DataFrame(gc, columns = columns)

gc_df.to_csv('Atiku_SA.csv',sep=',', encoding='utf-8')

