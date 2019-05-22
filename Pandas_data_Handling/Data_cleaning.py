#!/usr/bin/env python
# coding: utf-8

# ## Cleaning data having missing and duplicate values

# In[1]:


## Introduction ##


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[3]:


happiness2015 = pd.read_csv('World_Happiness_2015.csv')
happiness2016 = pd.read_csv('World_Happiness_2016.csv')
happiness2017 = pd.read_csv('World_Happiness_2017.csv')

happiness2015['YEAR'] = 2015
happiness2016['YEAR'] = 2016
happiness2017['YEAR'] = 2017

shape_2015 = happiness2015.shape
shape_2016 = happiness2016.shape
shape_2017 = happiness2017.shape


# ## Identifying Missing Values ##

# In[4]:


missing_2016 = happiness2016.isnull().sum()
missing_2017 = happiness2017.isnull().sum()


# In[5]:


print(missing_2016)


# In[6]:


print(missing_2017)


# ## Correcting Data Cleaning Errors that Result in Missing Values ##

# In[7]:


happiness2017.columns = happiness2017.columns.str.replace('.', ' ').str.replace('\s+', ' ').str.strip().str.upper()
happiness2015.columns = happiness2015.columns.str.replace(r'[\(\)]', '').str.strip().str.upper()
happiness2016.columns = happiness2016.columns.str.replace(r'[\(\)]', '').str.strip().str.upper()

combined = pd.concat([happiness2015, happiness2016, happiness2017], ignore_index=True, sort = True)
missing = combined.isnull().sum()
print(missing)


# ## Visualizing Missing Data ##

# In[8]:


regions_2017 = combined[combined['YEAR']==2017]['REGION']
missing = regions_2017.isnull().sum()
print(missing)


# ## Using Data From Additional Sources to Fill in Missing Values ##

# In[9]:


region2015 = happiness2015[['COUNTRY', 'REGION']]
region2016 = happiness2016[['COUNTRY', 'REGION']]

regions = pd.merge(left = region2015, right = region2016, how = 'left')
    
    
combined = pd.merge(left=combined, right=regions, on='COUNTRY', how='left')
combined = combined.drop('REGION_x', axis = 1)
missing = combined.isnull().sum()


# ## Identifying Duplicates Values ##

# In[10]:


combined['COUNTRY'] = combined['COUNTRY'].str.upper()
dups = combined.duplicated(['COUNTRY', 'YEAR'])
print(combined[dups])


# ## Correcting Duplicates Values ##

# In[11]:


combined['COUNTRY'] = combined['COUNTRY'].str.upper()
combined = combined.drop_duplicates(['COUNTRY', 'YEAR'])


# ## Handle Missing Values by Dropping Columns ##

# In[12]:


columns_to_drop = ['LOWER CONFIDENCE INTERVAL', 'STANDARD ERROR', 'UPPER CONFIDENCE INTERVAL', 'WHISKER HIGH', 'WHISKER LOW']
combined = combined.drop(columns_to_drop, axis = 1)
missing = combined.isnull().sum()


# ## Handle Missing Values by Dropping Columns Continued ##

# In[13]:


combined = combined.dropna(thresh=159, axis=1)
missing = combined.isnull().sum()


# ## Handling Missing Values with Imputation ##

# In[14]:


happiness_mean = combined['HAPPINESS SCORE'].mean()
print(happiness_mean)
combined['HAPPINESS SCORE UPDATED'] = combined['HAPPINESS SCORE'].fillna(happiness_mean)
print(combined['HAPPINESS SCORE UPDATED'].mean())


# ## Dropping Rows ##

# In[15]:


combined = combined.dropna()
missing = combined.isnull().sum()


# In[16]:


missing


# In[17]:


combined

