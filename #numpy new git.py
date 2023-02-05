#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
a = np.array([[1,2],
             [3,4]])


# In[3]:


a


# In[4]:


a1 = np.array([1,2],ndmin = 4)


# In[5]:


a1


# In[6]:


np.asanyarray([1,2,3,4,5])


# In[8]:


#always returns 2d array
np.mat([1,2,3])


# In[10]:


np.fromfunction(lambda i , j : i==j,(3,3))


# In[11]:


np.fromfunction(lambda i , j : i*j,(4,4))


# In[14]:


a =np.fromfunction(lambda i , j ,z : i*j*z,(3,3,2),dtype=int)


# In[15]:


a


# In[16]:


a.ndim


# In[17]:


a.shape


# In[18]:


a.size


# In[19]:


a.dtype


# In[23]:


a = np.fromfunction(lambda i , j : i*j,(4,3),dtype = int)


# In[24]:


a


# In[25]:


pd.DataFrame(a)


# In[26]:


np.random.rand(100,4)


# In[33]:


np.random.randint(4,50)


# In[ ]:




