# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 09:24:39 2023

@author: Arun Kumar
"""
# Import numpy, pandas, seaborn & matplotlib under its usual
import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

# Create a DataFrame from amazon csv file.
df_amazon = pd.read_csv(r'C:\Users\Arun Kumar\Desktop\uni\amazon.csv')
print(df_amazon)


df_amazon['discounted_price'] = df_amazon['discounted_price'].str.replace('₹' , '')
df_amazon['discounted_price'] = df_amazon['discounted_price'].str.replace(',' , '')
df_amazon['actual_price'] = df_amazon['actual_price'].str.replace('₹' , '')
df_amazon['actual_price'] = df_amazon['actual_price'].str.replace(',' , '')
df_amazon['discount_percentage'] = df_amazon['discount_percentage'].str.replace('%' , '')
df_amazon['rating_count'] = df_amazon['rating_count'].str.replace(',' , '')

print(df_amazon['rating'].unique())
df_amazon.drop(index=1279 , inplace= True)

def processing(j):
  df_amazon.iloc[:,j]=df_amazon.iloc[:,j].astype('float64') 
  col_mean=df_amazon.iloc[:,j].mean()
  df_amazon['rating_count'] = df_amazon.iloc[:,j].fillna(col_mean)

for i in range(3,8):
  processing(i)
print(df_amazon)

# create a Line plot between the relationship of discounted_price & rating_count. 
x, y = zip(*sorted(zip(df_amazon['discounted_price'], df_amazon['rating_count'])))
plt.plot(x,y)
plt.ylabel(df_amazon.columns[7], fontsize=16)
plt.xlabel(df_amazon.columns[3], fontsize=16)
plt.show()

# We can create a basic heatmap using the sns.heatmap() function:
plt.title('Corelation', fontsize=14)

# Set the legend
plt.legend(loc='best', fontsize=18)

# Default the colorbar from heatmap
p1 = sns.heatmap(df_amazon.corr(),cmap='Blues',annot = True)

# Describing the Bar Graph Relationship between Number of products & Rating 
df_amazon['rating'].value_counts().plot.bar()
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Products')
plt.show()