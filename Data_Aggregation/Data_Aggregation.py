## Introduction to the Data ##

import pandas as pd
import matplotlib.pyplot as plt
happiness2015 = pd.read_csv('World_Happiness_2015.csv')
first_5 = happiness2015.head()
info = happiness2015.info()


## Using Loops to Aggregate Data ##

mean_happiness = {}
unique = happiness2015['Region'].unique()
for i in unique:
    region_group = happiness2015[happiness2015['Region'] == i]
    region_mean = region_group['Happiness Score'].mean()
    mean_happiness[i] = region_mean

## Creating GroupBy Objects ##

grouped = happiness2015.groupby('Region')

aus_nz = grouped.get_group('Australia and New Zealand')

## Exploring GroupBy Objects ##

grouped = happiness2015.groupby('Region')
north_america = happiness2015.iloc[[4,14]]
na_group = grouped.get_group('North America')

equal = na_group == north_america

## Common Aggregation Methods with Groupby ##

grouped = happiness2015.groupby('Region')
means = grouped.mean()

## Aggregating Specific Columns with Groupby ##

grouped = happiness2015.groupby('Region')
happy_grouped = grouped['Happiness Score']
happy_mean = happy_grouped.mean()

## The Agg() Method ##

import numpy as np
grouped = happiness2015.groupby('Region')
happy_grouped = grouped['Happiness Score']
def dif(group):
    return (group.max() - group.mean())

happy_mean_max = happy_grouped.agg([np.mean, np.max])
mean_max_dif = happy_grouped.agg(dif)

## Computing Multiple and Custom Aggregations with the Agg() Method ##

happiness_means = happiness2015.groupby('Region')['Happiness Score'].mean()
happiness_means = happiness2015.groupby('Region')['Happiness Score'].mean()
print(happiness_means)

## Aggregation with Pivot Tables ##

pv_happiness = happiness2015.pivot_table(values='Happiness Score', index='Region', aggfunc=np.mean, margins=True)
pv_happiness.plot(kind = 'barh', xlim = (0,10), title = 'Mean Happiness Scores by Region', legend = False)
plt.show()
world_mean_happiness = happiness2015['Happiness Score'].mean()

## Aggregating Multiple Columns and Functions with Pivot Tables ##

grouped = happiness2015.groupby('Region')['Happiness Score', 'Family']
happy_family_stats = grouped.agg([np.min, np.max, np.mean])


pv_happy_family_stats = happiness2015.pivot_table(['Happiness Score', 'Family'], 'Region', aggfunc = [np.min, np.max, np.mean], margins = True)
