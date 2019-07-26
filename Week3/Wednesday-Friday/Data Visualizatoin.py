#Author:Johana Verdin
#File:Data Visualization
#Date Created: 06/26/2019

'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("tweets_small.json")
tweetData = json.load(tweetFile)
tweetFile.close()

#Create a list for polarity and subjectivity.
polarityList=[]

subjectivityList=[]


# Continue your program below! 
for tweet in tweetData:
    tweetTB = TextBlob(tweet["text"])

    polarityList.append(tweetTB.polarity)
    subjectivityList.append(tweetTB.subjectivity)

amount=len(polarityList)
total= 0
for i in polarityList:
    total+=i
average= total/amount
print("The average of polarity is...")
print(average)

amountsub=len(subjectivityList)
totalsub=0
for i in subjectivityList:
    totalsub+= i
averagesub=totalsub/amountsub
print("The average of subjectivity is...")
print(averagesub)


plt.hist(polarityList, bins=[-1,-0.5,0.0,0.5,1])
plt.xlabel("polarity")
plt.ylabel("polarity Level")
plt.title('Histogram of Numbers')
plt.grid(True)
plt.show()

plt.hist(subjectivityList, bins=[-1,-0.5,0.0,0.5,1])
plt.xlabel("subjectivity")
plt.ylabel("Subjectivity level")
plt.title('Histogram of Numbers')
plt.grid(True)
plt.show()

a_big_word=""

for j in range(70):
    a_big_word+=''+tweetData[j]['text']


commonwords=["about", "the", "it","but","an","a", "and", "like","https","http"]
filteredWords={}
monty=TextBlob(a_big_word)
wordlist=monty.words
for a in wordlist:
    if len(a)<3:
        continue
    if a in commonwords:
        continue
    if not a.isalpha(): 
        continue
    filteredWords[a]=monty.word_counts[a]
    
WordC= WordCloud().generate_from_frequencies(filteredWords.items())
plt.subplot(111)
plt.imshow(WordC, interpolation='bilinear')
plt.title(a_big_word)
plt.axis("off")
plt.figure(1)
plt.show()
