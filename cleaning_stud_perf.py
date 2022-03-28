import os
import re
import pandas as pd 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sb

#Opening the file
with open('StudentsPerformance.csv') as file:
    studperf_df = pd.read_csv(file)

#Checking the number of rows and columns
print('# of rows: {}, # of columns {}'.format(
    studperf_df.shape[0], studperf_df.shape[1]))

#Copying the dataframe and Cleaning the data (checking for NaN values and such)
new_per_df = studperf_df.copy()
working_columns = ['gender','race/ethnicity', 'parental level of education',
                   'lunch', 'test preparation course', 'math score', 
                   'reading score','writing score']
new_per_df = new_per_df[working_columns]

#Assessing invalid values
col = new_per_df.select_dtypes(include=['float64', 'int64']).columns
print(col)

invalid_list = list()
for i in col:
    y = any(x < 0 for x in new_per_df[i])
    if y == True:
        invalid_list.append(y)
print('# of negative values in the data frame {}.'.format(
    len(invalid_list)))

#Inconsistent Values Check
print(new_per_df.describe())

#Checking Zero values, Found one zero value
zero_values = (new_per_df[new_per_df.loc[0:]==0]).count().sum()
print('How many zero values are in this dataset? {}'.format(zero_values))

#Replacing the Zero Values with NaN, this should resolve the zero value issue
new_per_df.replace(0, np.nan, inplace=True)
new_zero = new_per_df[new_per_df.loc[0:]==0].count().sum()
print('How many zero values are in this dataset? {}'.format(new_zero))

#Showing the different columns before cleaning (will help with formatting)
print(new_per_df.columns)

#Formating
def remove_space(col):
    """Removing spaces between the column names and replacing them with '_'.

    Args:
        col: An argument that corresponds to the column name. 
    """
    cleaned_list = list()
    words_col = col.split()
    size = int(len(words_col))
    
    for i in range(len(words_col)):
        if i < size - 1:
            cleaned_list.append(words_col[i] + '_')
        else:
            cleaned_list.append(words_col[i])
    sep = ''
    result = sep.join(cleaned_list)
    
    return result

def remove_sp_char(col):
    """Replaces special characters. This one checks all the cases in which a 
    special character may occur. 

    Args:
        col: The name of the column.
    Returns:
        The updated column name
    """
    
    if "'" in col:
        col = col.replace("'",'')
    if "," in col:
        col = col.replace(",",'')
    if "_-_" in col:
        col = col.replace("_-_",'_')
    if "/" in col:
        col = col.replace("/",'_')
    if ":" in col:
        col = col.replace(":",'')
    if "-" in col:
        col = col.replace("-",'_')
        
    return col

#Changing capitalized letters
new_colhead = list()
col_head = new_per_df.columns

for col in col_head:
    new_header = remove_space(col)
    new_header = new_header.casefold()
    new_header = remove_sp_char(new_header)
    
    new_colhead.append(new_header)
    
#Showing the new columns of the dataframe
new_per_df.columns = new_colhead
print(new_per_df.columns)



