import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io
from sklearn.datasets import load_breast_cancer
from flask import (Flask, send_file, make_response)
from matplotlib import style

style.use('ggplot')

buhari_data = pd.read_csv("Buhari_SA.csv")
atiku_data = pd.read_csv("Atiku_SA.csv")

buhari_positive = []
buhari_negative = []
buhari_neutral = []

atiku_positive = []
atiku_negative = []
atiku_neutral = []

label = ['Positive Buhari', 'Negative Buhari','Positive Atiku', 'Negative Atiku']


def Average(lst): 
    return sum(lst) / len(lst) 
  

for index, row in buhari_data.iterrows():
    if(row['Score']) > 0:
        buhari_positive.append(row['Score'])
        #print('')
    elif(row['Score']) == 0:
        buhari_neutral.append(row['Score'])
        #print('')
    else:
        buhari_negative.append(row['Score'])

for index, row in atiku_data.iterrows():
    if(row['Score']) > 0:
        atiku_positive.append(row['Score'])
        #print('')
    elif(row['Score']) == 0:
        atiku_neutral.append(row['Score'])
        #print('')
    else:
        atiku_negative.append(row['Score'])


x = np.arange(len(label))


y = [Average(buhari_positive),Average(buhari_negative),Average(atiku_positive),Average(atiku_negative)]


#print(Average(atiku_negative))
barlist = plt.bar(x,y,color='r',align='center')


barlist[1].set_color('b')
barlist[3].set_color('b')

plt.title('Sentiment Scores')
plt.ylabel('Scores  ')
plt.xlabel('Candidate')
plt.xticks(x, label, fontsize=8)
#plt.xticks(x1, label1, fontsize=10, rotation=30)
plt.show()
#print(data['Score'].mean)