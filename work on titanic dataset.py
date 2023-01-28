#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')


# In[5]:


type(df)


# In[6]:


df


# In[19]:


dtypes = df.dtypes
col_name = df.dtypes[df.dtypes == object]


# In[20]:


col_name


# In[21]:


a = [x for x in range(10)].index


# In[22]:


a


# In[ ]:





# In[28]:


df['ineuron']= 'sab'


# In[26]:


df


# In[30]:


df.Name[0:15]


# In[31]:


df.describe()


# In[32]:


df


# In[36]:


s = df[df['Age'].isnull() == True].index


# In[ ]:





# In[42]:


df[df['Fare']==max(df['Fare'])]


# In[43]:


df[df['Fare']==max(df['Fare'])]['Name']


# In[48]:


count = 0
x = df[df['Sex']=='male']
for i in x:  
    count +=1
print(count)


# In[49]:


df[df['Sex']=='male']


# In[51]:


df.count()


# In[53]:


a = df.groupby('Sex')


# In[ ]:





# In[ ]:





# In[ ]:




