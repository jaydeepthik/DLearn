#!/usr/bin/env python
# coding: utf-8

"""
@authors: jaydeep thik , Vasudev Purandare

"""

# In[189]:


import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi

import urllib.request
from gensim.models import Word2Vec
import wikipedia
import nltk
from nltk.corpus import stopwords
import bs4
import requests
    


def call_rec(sub, vid_id, seek_time):
    print("SEEK_TIME:"+seek_time)
    seek_time = int(seek_time)
    topic=sub.split()[0].lower()
    #nltk.download('punkt')
    #nltk.download('averaged_perceptron_tagger')
    #nltk.download('stopwords')
    dict=YouTubeTranscriptApi.get_transcript(vid_id,languages=['en'])
    transcript=''
    for i in range(len(dict)):
        if dict[i]['start']<seek_time:
            transcript=transcript+' '+dict[i]['text']
        else:
            break
    print(transcript)
    p = wikipedia.page(sub)
    #print(p.url)
    #print(p.title)
    content = p.content
    
    stop_words = set(stopwords.words('english')) 
    text= content + transcript
    text = ' '.join([word.lower() for word in text.split() if word.lower() not in stop_words and len(word)>2])
    #print('the' in text.split())
    
    data = [] 
    from nltk.tokenize import sent_tokenize, word_tokenize
    
    # iterate through each sentence in the file 
    f = text.replace("\n", " ").replace(",","").replace("(","").replace(")","").replace(";","")
    
    for i in sent_tokenize(f): 
        temp = []       
        # tokenize the sentence into words 
        for j in word_tokenize(i): 
            if(j.isalpha() and j.lower() not in stop_words):
                temp.append(j.lower()) 
      
        data.append(temp) 
    
    #print('the' in data)  
    # Create CBOW model 
    model1 = Word2Vec(data, min_count = 1,  
                                  size = 100, window = 10) 
    
    model1.train(data, total_examples=1, epochs=50)
    
    #print("the" in model1.wv.vocab)
    topic_relevant=[]
    for t in model1.wv.most_similar(topic):
        topic_relevant.append(t[0])
    
    
    #print(topic_relevant) 
    about_topics=''
    for topics in topic_relevant:
        #print("***"+topics)
        response = requests.get("https://en.wikipedia.org/wiki/"+topics)

        about_topics +=topics+' :'

        if response is not None:
            html = bs4.BeautifulSoup(response.text, 'html.parser')
            paragraphs = html.select("p")
            #print(wikipedia.page(topics).content)
            for para in paragraphs:
                #print("##########################")
                #print(para.text)
                if len(para.text.split())>20:
                    about_topics=about_topics+para.text
                    break
            about_topics=about_topics+'\n'
        response.close();

    print(topic_relevant)
    return about_topics
    """
    for i in range(len(dict)):
        for w in topic_relevant:
            if w in dict[i]['text'].lower() :
                print (dict[i]['text'])
    
    """