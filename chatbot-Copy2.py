#!/usr/bin/env python
# coding: utf-8

# In[12]:


import nltk
nltk.download('punkt')


# In[13]:


get_ipython().system('pip install newspaper3k')


# In[14]:


from newspaper import Article
import random
import string 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[15]:


article=Article('https://www.who.int/news-room/fact-sheets/detail/depression')
article.download()
article.parse()
article.nlp()
a=article.text


# In[16]:


article2=Article('https://www.healthline.com/health/depression/help-for-depression')
article2.download()
article2.parse()
article2.nlp()
b=article2.text


# In[17]:


corpus=a+b


# In[18]:


print(corpus)


# In[19]:


text=corpus
sentence_list=nltk.sent_tokenize(text)


# In[20]:


print(sentence_list)


# In[21]:


def greeting_response(text):
    text=text.lower()
    
    bot_greetings=['hi,how can i help you?','hello,how can i help you?','aloha,how can i help you?','*nods*,how can i help you?','howdy,how can i help you?','hey,how can i help you?',]
    user_greetings=['hi','hey','greetings','hi-ya','bonjour','hello','sup']
    
    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)


# In[22]:


def index_sort(list_var):
    length=len(list_var)
    list_index=list(range(0, length))
    
    x=list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                temp=list_index[i]
                list_index[i]=list_index[j]
                list_index[j]=temp
                
                
    return list_index


# In[23]:


def bot_response(user_input):
    user_input=user_input.lower()
    sentence_list.append(user_input)
    bot_response=''
    cm=CountVectorizer().fit_transform(sentence_list)
    similarity_scores=cosine_similarity(cm[-1], cm)
    similarity_scores_list=similarity_scores.flatten()
    index=index_sort(similarity_scores_list)
    index=index[1:]
    response_flag=0
    
    j=0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response=bot_response+' '+sentence_list[index[i]]
            response_flag=1
            j=j+1
        if j > 2:
            break
            
    if response_flag==0:
        bot_response=bot_response+' '+"I apologize, I don,t understand."
        
    sentence_list.remove(user_input)
    
    return bot_response


# In[24]:


import urllib.parse


# In[25]:


get_ipython().system('pip install sty')
from sty import fg, bg, ef, rs


# In[27]:


print('friend bot: I am your friend i can help you out. you can ask me any quiries related to depression. if u want to exit, type bye')

exit_list=['exit','see you later','bye','quit','break']

while(True):
    user_input=input()
    if user_input.lower() in exit_list:
        a="friend bot: It was nice chatting with you . If u still feel alone or need help here are helplines:"
        b=fg.red+"National Suicide Prevention Lifeline: 1-800-273-8255 (24X7)"+fg.rs
        c=fg.red+"Mental health helpline: 1860-266-2345 (24X7)"+fg.rs
        d= urllib.parse.quote ('suicidepreventionlifeline.org/chat/')
        g="or"
        e='CHAT ONLINE:'
        f='https://'+ d
        print(a)
        print(b)
        print(c)
        print(g)
        print(e)
        print(f)
        break
    else:
        if greeting_response(user_input) != None:
            print('friend bot:' +greeting_response(user_input))
        else:
            print('friend bot: '+bot_response(user_input))


# In[ ]:


hi

