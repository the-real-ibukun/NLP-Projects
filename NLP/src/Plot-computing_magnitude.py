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

buhari_magnitude = []
atiku_magnitude = []

label = ['Buhari','Atiku']

def Average(lst): 
    return sum(lst) / len(lst) 
  
for index, row in buhari_data.iterrows():
   buhari_magnitude.append(row['Magnitude'])

for index, row in atiku_data.iterrows():
    atiku_magnitude.append(row['Magnitude'])

    
x = np.arange(len(label))


y = [Average(buhari_magnitude),Average(atiku_magnitude)]

#print(Average(atiku_negative))
barlist = plt.bar(x,y,color='r',align='center')

barlist[1].set_color('b')


plt.title('Average Magnitude')
plt.ylabel('Values')
plt.xlabel('Candidate')
plt.xticks(x, label, fontsize=8)
#plt.xticks(x1, label1, fontsize=10, rotation=30)
plt.show()
#print(data['Score'].mean)

