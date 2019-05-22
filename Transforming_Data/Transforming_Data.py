#!/usr/bin/env python
# coding: utf-8

# ## Data Transformation with Pandas

# ## Introduction ##

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

happiness2015 = pd.read_csv('World_Happiness_2015.csv')
mapping = {'Economy (GDP per Capita)': 'Economy', 'Health (Life Expectancy)': 'Health', 'Trust (Government Corruption)': 'Trust' }

happiness2015 = happiness2015.rename(mapping, axis = 1)


# ## Apply a Function Element-wise Using the Map and Apply Methods ##

# In[2]:


def label(element):
    if element > 1:
        return 'High'
    else:
        return 'Low'
    
economy_impact_map = happiness2015['Economy'].map(label)
economy_impact_apply = happiness2015['Economy'].apply(label)
equal = economy_impact_map.equals(economy_impact_apply)


# ## Apply a Function Element-wise Using the Map and Apply Methods Continued ##

# In[3]:


def label(element, x):
    if element > x:
        return 'High'
    else:
        return 'Low'
economy_impact_apply = happiness2015['Economy'].apply(label, x = 0.8)


# ## Apply a Function Element-wise to Multiple Columns Using Applymap Method ##

# In[4]:


def label(element):
    if element > 1:
        return 'High'
    else:
        return 'Low'
economy_apply = happiness2015['Economy'].apply(label)
factors = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity']
factors_impact = happiness2015[factors].applymap(label)


# ## Apply Functions along an Axis using the Apply Method ##

# In[5]:


def v_counts(col):
    num = col.value_counts()
    den = col.size
    return num/den

v_counts_pct = factors_impact.apply(v_counts)


# ## Apply Functions along an Axis using the Apply Method Continued ##

# In[6]:


factors = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity', 'Dystopia Residual']

def percentages(col):
    div = col/happiness2015['Happiness Score']
    return div*100
factor_percentages = happiness2015[factors].apply(percentages)


# ## Reshaping Data with the Melt Function ##

# In[7]:


main_cols = ['Country', 'Region', 'Happiness Rank', 'Happiness Score']
factors = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity', 'Dystopia Residual']
melt = pd.melt(happiness2015, id_vars = main_cols, value_vars = factors)
melt['Percentage'] = round(melt['value']/melt['Happiness Score'] * 100, 2)


# ## Aggregate the Data and Create a Visualization ##

# In[8]:


melt = pd.melt(happiness2015, id_vars = ['Country', 'Region', 'Happiness Rank', 'Happiness Score'], value_vars= ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity', 'Dystopia Residual'])
melt['Percentage'] = round(melt['value']/melt['Happiness Score'] * 100, 2)
pv_melt = melt.pivot_table(index='variable', values='value')
pv_melt.plot(kind='pie', y='value', legend=False)
plt.show()

