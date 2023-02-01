#!/usr/bin/env python
# coding: utf-8

# In[2]:


df


# In[3]:


df['Sex'].value_counts()


# In[1]:


import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')


# In[8]:


len(df[df['Sex'] == 'male'])


# In[9]:


import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')


# In[10]:


len(df[df['Sex'] =="male"])


# In[12]:


df.groupby('Sex')['Sex'].count()


# In[14]:


df['Survived']==1


# In[15]:


df[df['Survived']==1]


# In[18]:


len(df[df['Survived']==1])


# In[20]:


df[df['Survived']==0]


# In[21]:


len(df[df['Survived']==0])


# In[22]:


df['Age'] == df['Age'].max()


# In[23]:


df[df['Age'] == df['Age'].max()]


# In[24]:


df['Pclass'].value_counts()


# In[26]:


df['Pclass'].value_counts()


# In[27]:


df["Name"]


# In[28]:


df['Name'].str


# In[31]:


df['Name'].str.startswith("S")


# In[33]:


df[df['Name'].str.startswith("S")]


# In[34]:


df.groupby('Pclass')['Pclass'].count()


# In[36]:


df['New coloumn'] = df['SibSp'] + df['Parch']


# In[37]:


df.head()


# In[38]:


df['Age']<25


# In[39]:


df[df['Age'] < 25]


# In[48]:


#checking multiples colomns based on conditions
(df['Survived'] ==0) & (df["Age" ]< 40 )


# In[50]:


df[(df['Survived'] == 0) & (df['Age'] < 40)]


# In[52]:


len(df[(df['Age']<40) & df['Survived']==0])


# In[57]:


#separating strings and numbers in cabin coloumn
#import regular expression module
import re
replace = re.compile("([a-zA-Z]+)")
df['string_cabin_list'] = df['Cabin'].str.extract(replace)
df['num_cabin_list'] = df['Cabin'].str.replace(replace,"")


# In[58]:


df['string_cabin_list']


# In[4]:


import pandas as pd
df = pd.read_csv('b.csv',sep = ';')


# In[5]:


df


# In[6]:


df.head(5)


# In[7]:


df['campaign']


# In[8]:


df['campaign'].unique()


# In[9]:


list(df['campaign'].unique())


# In[10]:


set(list(df['campaign'].unique()))


# In[12]:


(df['housing'] =='yes') & (df['loan']=='yes')


# In[26]:


df2 = df[(df['housing'] =='yes') & (df['loan']=='yes')]


# In[17]:


len(df[(df['housing']=='yes') & (df['loan']=='yes')])


# In[18]:


df['age'] < 60


# In[22]:


df[df['age'] > 60]


# In[23]:


len(df[df['age'] > 60])


# In[24]:


df['month']


# In[25]:


max(df['month'])


# In[27]:


df2 


# In[29]:


df.groupby(['contact','y']).count()


# In[30]:


df_grp = df.groupby(['contact','y']).count()


# In[35]:


df_grp.loc['cellular']


# In[37]:


len(df_grp['campaign'].unique())


# In[40]:


df[df['job'] == 'entrepreneur']
#  to find how many ?? find the length of  df


# In[41]:


df[df['balance']<0]


# In[42]:


df.groupby('education')


# In[43]:


df.groupby('education').count()


# In[44]:


df


# In[45]:


df['campaign'].unique


# In[61]:


df[df['housing'] == 'yes' ]


# In[62]:


len(df[df['housing'] == 'yes' ])


# In[63]:


len(df[df['loan']=='yes'])


# In[64]:


df


# In[68]:


max(df['month'])


# In[ ]:


month = df['month']
count = 0

for i in month:
    
    


# In[74]:


df[df['age'] >= 60]


# In[75]:


len(df[df['age'] >= 60])


# In[76]:


df


# In[77]:


df['job']=='entrepreneur'


# In[78]:


df[df['job']=='entrepreneur']


# In[80]:


len(df[df['job']=='entrepreneur'])


# In[83]:


df[df['balance']<0]


# In[85]:


len(df[df['balance']<0])


# In[86]:


len(df)


# In[87]:


len(df[df['balance']>0])


# In[88]:


edu = df[df['education']=='primary'] + df[df['education']=='secondary'] + df[df['education']=='tertiary']


# In[89]:


edu


# In[93]:


df[df['education']=='primary']


# In[94]:


month = df['month']


# In[95]:


max(df['month'])


# In[ ]:


max = jan
for i in month:

    

