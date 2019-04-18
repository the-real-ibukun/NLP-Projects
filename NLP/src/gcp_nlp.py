from tqdm import tqdm # This is an awesome package for tracking for loops
import pandas as pd
from google.cloud import language
import json



with open('data.json') as json_data:
    data = json.load(json_data)

for i in data:
    print(i['comments'])



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


gc_results = [gc_sentiment(row['comments']) for row in tqdm(data, ncols = 100)]
gc_score, gc_magnitude = zip(*gc_results) # Unpacking the result into 2 lists
gc = list(zip((row['response'] for row in data),(row['comments'] for row in data), gc_score, gc_magnitude))
columns = ['Candidate','Response', 'Score', 'Magnitude']
gc_df = pd.DataFrame(gc, columns = columns)

gc_df.to_csv('Prod_SA.csv',sep=',', encoding='utf-8')
