import pandas as pd
import csv
import nltk
import os.path as checkcsv

def analyze(comment_file):

    dataset = pd.read_csv(comment_file, encoding_errors = 'ignore')
    dataset = dataset.iloc[:, 0:]


    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    analyser = SentimentIntensityAnalyzer()

    def vader_sentiment_result(sent):
        scores = analyser.polarity_scores(sent)

        if scores["neg"] > scores["pos"]:
            return 0
        return 1

    dataset['vader_sentiment'] = dataset['Comment'].apply(lambda x : vader_sentiment_result(x))


    for (sentiment), group in dataset.groupby(['vader_sentiment']):
         group.to_csv(f'{sentiment}.csv', index=False)
    
    if checkcsv.exists('1.csv') == False:
        with open('1.csv', 'w', encoding='UTF8', newline='') as f1:
            writer1 = csv.writer(f1)
            header1 = ['Empty', 'Empty', 'Empty']
            row1 = ['No Positive Comments', 'No Positive Comments', 'No Positive Comments']
            writer1.writerow(header1)
            writer1.writerow(row1)

    if checkcsv.exists('0.csv') == False:
        with open('0.csv', 'w',encoding='UTF8', newline='') as f0:
            writer0 = csv.writer(f0)
            header0 = ['Empty', 'Empty', 'Empty']
            row0 = ['No Negative Comments', 'No Negative Comments', 'No Negative Comments']
            writer0.writerow(header0)
            writer0.writerow(row0)
    
    pos = (pd.read_csv("1.csv", engine = 'python')).iloc[:, :-1]
    neg = (pd.read_csv("0.csv", engine = 'python')).iloc[:, :-1]

    positive_comments = pos.to_csv("Positive Comments.csv", index=False)
    negative_comments = neg.to_csv("Negative Comments.csv",index=False)

    video_positive_comments = str(len(pos.axes[0])) + ' Comments'
    video_negative_comments = str(len(neg.axes[0])) + ' Comments' 
    
    if (pd.read_csv('1.csv', nrows=0).columns.tolist())[0] == 'Empty':
        video_positive_comments = '0 Comments'
    if (pd.read_csv('0.csv', nrows=0).columns.tolist())[0] == 'Empty':
        video_negative_comments = '0 Comments'

    return positive_comments, negative_comments, video_positive_comments, video_negative_comments
