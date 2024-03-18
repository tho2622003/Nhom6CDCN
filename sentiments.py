import numpy as np
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

sia = SentimentIntensityAnalyzer()
df = pd.read_csv('FLAT.csv', encoding_errors = 'ignore')
df['scores'] = df['comment'].apply(lambda body: sia.polarity_scores(str(body)))
df.head()
df['compound'] = df['scores'].apply(lambda score_dict:score_dict['compound'])
df.head()
df['pos'] = df['scores'].apply(lambda pos_dict:pos_dict['pos'])
df.head()
df['neg'] = df['scores'].apply(lambda neg_dict:neg_dict['neg'])
df.head()
df['type']=''
df.loc[df.compound>0,'type']='POS'
df.loc[df.compound==0,'type']='NEUTRAL'
df.loc[df.compound<0,'type']='NEG'
df.head()
len=df.shape
(rows,cols)=len
pos=0
neg=0
neutral=0
for i in range(0,rows):
    if df.loc[i][5]=="POS":
        pos=pos+1
    if df.loc[i][5]=="NEG":
        neg=neg+1
    if df.loc[i][5]=="NEUTRAL":
        neutral=neutral+1

print("Positive :"+str(pos) + "  Negative :" + str(neg) + "   Neutral :"+ str(neutral))

# histogram sentiments
plt.hist(df['compound'])
plt.title("Comment Sentiment Analysis")
plt.show()

print("Average Positive: ", df['pos'].mean(), "\n")
print("Average Negative: ", df['neg'].mean(), "\n")
print("Average Compound: ", df['compound'].mean(), "\n")