#!/usr/bin/env python
# coding: utf-8

# # Working With Strings In Pandas

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# ## Introduction ##

# In[7]:


world_dev = pd.read_csv("World_dev.csv")
happiness2015 = pd.read_csv('World_Happiness_2015.csv')
col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}
merged = pd.merge(left = happiness2015, right = world_dev, how = 'left', left_on = 'Country', right_on = 'ShortName')
merged = merged.rename(col_renaming, axis = 1)


# ## Using Apply to Transform Strings ##

# In[8]:


def extract_last_word(element):
    s = str(element)
    s_s = s.split()
    return s_s[-1]

merged['Currency Apply'] = merged['CurrencyUnit'].apply(extract_last_word)
print(merged['Currency Apply'].head)


# ## Vectorized String Methods Overview ##

# In[9]:


merged['Currency Vectorized'] = merged['CurrencyUnit'].str.split().str.get(-1)
print(merged['Currency Vectorized'].head())


# ## Exploring Missing Values with Vectorized String Methods ##

# In[10]:


lengths = merged['CurrencyUnit'].str.len()
value_counts = lengths.value_counts(dropna = False)


# ## Finding Specific Words in Strings ##

# In[11]:


pattern = r"[Nn]ational accounts"
national_accounts = merged['SpecialNotes'].str.contains(pattern)
print(national_accounts.head())


# ## Finding Specific Words in Strings Continued ##

# In[12]:


pattern = r"[Nn]ational accounts"
national_accounts = merged['SpecialNotes'].str.contains(pattern, na = False)
merged_national_accounts = merged[national_accounts]
print(merged_national_accounts.head())


# ## Extracting Substrings from a Series ##

# In[13]:


pattern =r"([1-2][0-9]{3})"
years = merged['SpecialNotes'].str.extract(pattern)


# ## Extracting Substrings from a Series Continued ##

# In[14]:


pattern = r"([1-2][0-9]{3})"
years = merged['SpecialNotes'].str.extract(pattern, expand=True)


# ## Extracting All Matches of a Pattern from a Series ##

# In[15]:


pattern = r"(?P<Years>[1-2][0-9]{3})"
years = merged['IESurvey'].str.extractall(pattern)
value_counts = years['Years'].value_counts()
print(value_counts)


# ## Extracting More Than One Group of Patterns from a Series ##

# In[16]:


pattern = r"(?P<First_Year>[1-2][0-9]{3})/?(?P<Second_Year>[0-9]{2})?"
years = merged['IESurvey'].str.extractall(pattern)
first_two_year = years['First_Year'].str[0:2]
years['Second_Year'] = first_two_year + years['Second_Year']


# ## Cleaning a String Column, Aggregate the Data, and Plot the Results ##

# In[17]:


merged['IncomeGroup'] = merged['IncomeGroup'].str.replace(' income', '').str.replace(':', '').str.upper()
pv_incomes = merged.pivot_table(values='Happiness Score', index='IncomeGroup')
pv_incomes.plot(kind='bar', rot=30, ylim=(0,10))
plt.show()


# In[ ]:




