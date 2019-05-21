#!/usr/bin/env python
# coding: utf-8

# # Data Combining

# ## Introduction ##

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


happiness2015 = pd.read_csv("World_Happiness_2015.csv")
happiness2016 = pd.read_csv('World_Happiness_2016.csv')
happiness2017 = pd.read_csv('World_Happiness_2017.csv')

happiness2015['Year'] = 2015
happiness2016['Year'] = 2016
happiness2017['Year'] = 2017


# ## Combining Dataframes with the Concat Function ##

# In[3]:


head_2015 = happiness2015[['Country','Happiness Score', 'Year']].head(3)
head_2016 = happiness2016[['Country','Happiness Score', 'Year']].head(3)
concat_axis0 = pd.concat([head_2015, head_2016], axis = 0)
concat_axis1 = pd.concat([head_2015, head_2016], axis = 1)

question1 = 6
question2 = 3


# ## Combining Dataframes with the Concat Function  different shape ##

# In[4]:


head_2015 = happiness2015[['Year','Country','Happiness Score', 'Standard Error']].head(4)
head_2016 = happiness2016[['Country','Happiness Score', 'Year']].head(3)

concat_axis0 = pd.concat([head_2015, head_2016], axis = 0, sort = True)

rows = 7
columns = 4


# ## Combining Dataframes with Different Shapes Using the Concat Function ##

# In[5]:


head_2015 = happiness2015[['Year','Country','Happiness Score', 'Standard Error']].head(4)
head_2016 = happiness2016[['Country','Happiness Score', 'Year']].head(3)
concat_update_index = pd.concat([head_2015, head_2016], axis = 0, ignore_index = True, sort = True)


# ## Joining Dataframes with the Merge Function ##

# In[6]:


three_2015 = happiness2015[['Country','Happiness Rank','Year']].iloc[2:5]
three_2016 = happiness2016[['Country','Happiness Rank','Year']].iloc[2:5]

merged = pd.merge(left = three_2015, right = three_2016, on = 'Country')


# ## Joining on Columns with the Merge Function ##

# In[7]:


three_2015 = happiness2015[['Country','Happiness Rank','Year']].iloc[2:5]
three_2016 = happiness2016[['Country','Happiness Rank','Year']].iloc[2:5]
merged = pd.merge(left=three_2015, right=three_2016, on='Country')

merged_left = pd.merge(left = three_2015, right = three_2016, on = 'Country', how = 'left')

merged_left_updated = pd.merge(left = three_2016, right = three_2015, on = 'Country', how = 'left')


# ## Left Joins with the Merge Function ##

# In[8]:


three_2015 = happiness2015[['Country','Happiness Rank','Year']].iloc[2:5]
three_2016 = happiness2016[['Country','Happiness Rank','Year']].iloc[2:5]
merged = pd.merge(left=three_2015, right=three_2016, how='left', on='Country')
merged_updated = pd.merge(left=three_2016, right=three_2015, how = 'left', on='Country')
merged_suffixes = pd.merge(left = three_2015, right = three_2016, how = 'left',
                           on = 'Country', suffixes = ('_2015', '_2016'))
merged_updated_suffixes = pd.merge(left=three_2016, right=three_2015, how = 'left', on='Country', suffixes = ('_2016', '_2015'))


# ## Join on Index with the Merge Function ##

# In[9]:


import pandas as pd
four_2015 = happiness2015[['Country','Happiness Rank','Year']].iloc[2:6]
three_2016 = happiness2016[['Country','Happiness Rank','Year']].iloc[2:5]
merge_index = pd.merge(left = four_2015,right = three_2016, left_index = True, right_index = True, suffixes = ('_2015','_2016'))

merge_index_left = pd.merge(left = four_2015, right = three_2016, left_index = True, right_index = True, how = 'left',suffixes = ('_2015','_2016'))
rows = 4
columns = 6


# ## Combining Data and Creating a Visualization ##

# In[10]:


happiness2017.rename(columns={'Happiness.Score': 'Happiness Score'}, inplace=True)
combined = pd.concat([happiness2015, happiness2016, happiness2017], axis = 0, sort = True)
pivot_table_combined = combined.pivot_table(index = 'Year', values = 'Happiness Score', aggfunc = np.mean)
pivot_table_combined.plot(kind = 'barh', title = 'Mean Happiness Scores by Year', xlim = (0,10))
plt.show()


# ## Conclusion:
# 

# - Mean Happiness Scores were retained
