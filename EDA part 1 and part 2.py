#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


#display all coloumns of  the dataframes
pd.pandas.set_option('display.max_columns',None)


# In[3]:


df = pd.read_csv('train.csv')


# In[4]:


df.head()


# In[5]:


#to find no. of rows and coloumns
df.shape


# In[6]:


# missing values
df.isnull().sum()


# In[7]:


df.isnull()


# In[8]:


for features in df.columns:
    print(df[features])


# In[9]:


df.columns


# In[10]:


features_with_na = [features for features in df.columns if df[features].isnull().sum()>=1]


# In[11]:


features_with_na


# In[12]:


for feature in features_with_na:
    print(feature,np.round(df[feature].isnull().mean()*100,4),'%missing values')


# In[13]:


for feature in features_with_na:
    print(feature,np.round(df[feature].isnull().mean(),4),'missing values')


# In[14]:


sns.boxenplot(df['SalePrice'])


# In[15]:


sns.boxplot(df['SalePrice'])


# In[16]:


#lets copy some amazing diagrams
data = df.copy()
for feature in features_with_na:
    
    #make variables that indicate 1 if the observation is missing or 0 otherwise
    data[feature]=np.where(data[feature].isnull(),1,0)
    
    #let's calculate the mean Saleprice where the information is missing or present
    data.groupby(feature)['SalePrice'].median().plot.bar()
    plt.title(feature)
    plt.show()
    


# In[17]:


df.info()


# In[18]:


##list of numerical variables
df['SaleType'].dtype!='O'


# In[19]:


numerical_features = [feature for  feature in  df.columns if df[feature].dtypes!='O']


# In[20]:


print(numerical_features)
print(len(numerical_features))
df[numerical_features].head()


# In[21]:


df.head()


# In[22]:


year_feature = [feature for feature in numerical_features if 'Yr' in feature or 'Year' in feature ]


# In[23]:


for feature in year_feature:
    print(feature,df[feature].unique())


# In[24]:


df.groupby('YrSold')['SalePrice'].median().plot()
plt.xlabel('year sold')
plt.ylabel('median house price')
plt.title('House price vs year sold')


# In[25]:


df.groupby('YrSold')['SalePrice'].median()


# In[26]:


#lets copy some amazing diagrams
data = df.copy()
for feature in features_with_na:
    
    #make variables that indicate 1 if the observation is missing or 0 otherwise
    data[feature]=np.where(data[feature].isnull(),1,0)
    
    #let's calculate the mean Saleprice where the information is missing or present
    data.groupby(feature)['SalePrice'].median().plot.bar()
    plt.title(feature)
    plt.show()
    


# In[27]:


numerical_features


# In[28]:


data = df.copy()
for features in numerical_features:
    data.grfeatures)['SalePrice'].median().plot()


# In[36]:


### comparing the difference between all years sales price and features
data = df.copy()
for feature in year_feature:
    if features!='YearSold':
        data[feature]!=data['Year']
        


# In[37]:


### Here we will compare the  all years features with Salesprice
data=df.copy()
for feature in year_feature:
    if feature!='YrSold':
        
        plt.scatter(data[feature],data['SalePrice'])
        plt.xlabel(feature)
        plt.ylabel('SalePrice')
        plt.show()
        


# In[ ]:


### Here we will compare the difference between all years features with Salesprice
data = df.copy()
for feature in year_feature:
    if feature!='YrSold':
        data[feature]=data['YrSold']-data[feature]
        plt.scatter(data[feature],data['SalePrice'])
        plt.xlabel(feature)
        plt.ylabel("sale price")
        plt.show()


# # observation:
# with all yearwise information we come to a conclusion that new houses are more costlier when compared to old houses
# ## looks like power law distributuion/pareto
# ### numerical variables-2types:
# 1) discrete
# 2) continuous

# In[38]:


discrete_feature=[feature for feature in numerical_features if len(df[feature].unique())<25]


# In[39]:


df[discrete_feature]


# In[40]:


data = df.copy()
for feature in discrete_feature:
    data.groupby(feature)['SalePrice'].median().plot(kind='bar')
    plt.xlabel(feature)
    plt.ylabel('SalePrice')
    plt.title(feature)
    plt.show()


# ## there is a relationship between Discrete feature  and Saleprice
# 

# In[41]:


continuous_feature=[feature for feature in numerical_features if feature not in discrete_feature+year_feature]


# In[42]:


len(continuous_feature)


# In[43]:


df[continuous_feature]


# In[44]:


data = df.copy()
for feature in continuous_feature:
    data.groupby(feature)['SalePrice'].median().plot.hist()
    plt.xlabel(feature)
    plt.ylabel('Saleprice')
    plt.title(feature)

    plt.show()


# In[46]:


data = df.copy()
for feature in continuous_feature:
    data[feature].hist(bins=25)
    plt.xlabel(feature)
    plt.ylabel('count')
    plt.title(feature)
    plt.show()


# # EDA PART-2

# In[49]:


try:
    data = df.copy()
    for feature in continuous_feature:
        if 0 in data[feature].unique():
            pass
        else:
            data[feature] = np.log(data['feature'])
            plt.scatter(data[feature],data['SalePrice'])
            plt.xlabel(feature)
            plt.ylabel('SalePrice')
            plt.title(feature)
            plt.show()
except Exception as exe:
    print(exe)


# In[50]:


### Outliers
for feature in continuous_feature:
    if 0 in data[feature].unique():
        pass
    else:
        data[feature]=np.log(data[feature])
        data.boxplot(column=feature)
        plt.ylabel(feature)
        plt.title(feature)
        plt.show()


# In[51]:


df['SalePrice'].hist()


# In[52]:


sns.histplot(df['SalePrice'],kde=True)


# # categorical variables

# In[66]:


categorical_features = [features for features in df.columns if df[features].dtype=='O']


# In[69]:


df[categorical_features].head()


# In[72]:


for feature in categorical_features:
    print(f'the feature name is {feature} and the number of categorical_variables are {len(df[feature].unique())}')


# In[74]:


### relationship between categorical_variables and sales price
data  = df.copy()
for feature in categorical_features:
    data.groupby(feature)['SalePrice'].median().plot.bar()
    plt.xlabel(feature)
    plt.ylabel('SalePrice')
    plt.title(feature)
    plt.show()


# In[ ]:




