#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Outlier processing
import pandas as pd  
import numpy as np  
from sklearn.preprocessing import Imputer  

# Generate missing data
out_dir = 'data/'
df = pd.read_csv(out_dir + 'StackOverFlow_2017.csv', skiprows=1, low_memory=False)

# Judging outliers by Z-Score method
df_zscore = df.copy()  # Copy a data frame to store the Z-score score
cols = df.columns  # get all columns from data frame
for col in cols:  # loop all columns
    df_col = df[col]  # get all column values
    z_score = (df_col - df_col.mean()) / df_col.std()  # calculate Z-score value per column
    df_zscore[col] = z_score.abs() > 2.2  # check if Z-score of current column is greater than 2.2，then True; otherwize, False.

# Delete the row where the outlier is in
df_drop_outlier = df[df_zscore['col1'] == False]


#save cleaned data into csv file
df.to_csv(out_dir + "cleaned_StackOverFlow.csv",index=False)

