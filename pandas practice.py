#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')


# In[5]:


col_name = df.dtypes[df.dtypes=='object'].index


# In[6]:


col_name


# In[7]:


df


# In[10]:


sex = col_name[col_name == 'Sex'].index


# In[11]:


sex


# In[13]:


sex = df['Sex']


# In[18]:


count = 0
for i in range(len(sex)):
    if sex[i] == 'male':
        count+=1


# In[17]:


sex


# In[19]:


count


# In[20]:


df


# In[23]:


sur = df['Survived']
count = 0
for i in range(len('sur')):
    if sur[i]=='1':
        count +=1
print('survived:',count)


# In[33]:


count = 0
for i in range(len(df['Survived'])):
    if df['Survived'][i] == 1:
        count+=1
print('SURVIVED:',count)


# In[27]:


a


# In[ ]:





# In[38]:


df


# In[39]:


age = df['Age']


# In[40]:


age


# In[43]:


count = 1
for i in range(len(age)):
    if age[i]>25:
        count +=1
print("people greater then 25 years of age:",count)


# In[46]:


sur = df['Survived']
count = 1
for i in range(len(sur)):
    if sur[i] == 0 and age[i]<40:
        count+=1
print(" person died whose age was less then 40 :",count)


# In[48]:


df


# In[63]:


cab=[]
cabtxt=[]
cabno=[]
cabin = df['Cabin']
for i in range(len(cabin)):
    if cabin[i] == 'NaN':
        break
    else:
        cab.append(i)


# In[64]:


cabin.index


# In[65]:


print(cabtxt)
print(cabno)


# In[66]:


cab


# In[67]:


cabin


# In[76]:


import pandas as pd
bank = pd.read_csv('b.csv',delimiter=';')


# In[77]:


bank


# In[ ]:




