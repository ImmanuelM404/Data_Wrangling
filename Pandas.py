#Panda 

# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np 
import os 

#Where our data lives 
# csv_path = os.path.join('..', 'collection-master', 'artwork_data.csv')
#Ask fo help on how the os.path.join works 

#Read just 5 rows to see what's there 
df = pd.read_csv('Annual_Statement_of_Economic_Interests__SEI__Form_700_-_Non-Filers (1).csv')
df
# print(df['district_name'])
# print(df.info)
print(df.shape)
print(df.describe)
print(df['Agency'].mode())
print(df.head())

#Select/Filter/Sort ------ Filter 
def select_rows():
    name = df.loc[4:19, 'Agency'].mode()
    names = df.loc[:, 'Agency'].mode()
    print(name)
    print(names)
select_rows()
#Boolean Filtering 
def bool_rows(): 
    # filter = df['Agency'] == 'Workforce Investment Board'
    # print(filter)
    filters = df[df['Agency'] == 'Workforce Investment Board']
    print(filters)
bool_rows()

#Sorting 
def sort_rows():
    sort = df.sort_values('Name')
    print(sort)
sort_rows()

#Cleaning Data 
print(df.isnull().any())
#Notes are null add a value to one of the notes 

#Transforming 
group_agency = df.groupby('Agency')
print(group_agency.mean())











#Notes 
    #Indexing: Single Value
    #Retrieve a column by label
    #This returns a Series
        # df['col_name'] if column index has type string 
        # df[5] if column has a type int 
    # retrieve cell from column and row 
        # df['col_name']['row_name']

    #Indexing: Lists and Slices 
    #Retrieve mulptile columns in any orderr
    # This returns a DataFrame 
        # df[['Time', 'Temp', 'Pressure']]
    #Slices return rows, not columns 
    #Also returns a DataFrame
        # df[2:35]
        # capitals['Palau':'Nauru'] #also works with label 

    #Indexing: loc 
    #DataFrame.loc does row-based indexing with labels 
    # Retrieve a single row 
        # df.loc['San Marino']
    # Select column in the same operations 
        # df.loc['San Marino', 'Population']
        # compare, selects the column then the row 
            # df['Population']['San Marino']

    # Indexing: iloc 
    # DataFrame.iloc does row-based indexing by position 
    # Retrieve a single row 
        # df.loc[5]
    #Select column in the same operations
        # df.iloc[4,2]
    #loc and iloc also support lists and slices 

#Boolean Filtering 
    # capitals[[True, True, False, True, False]] true returns the data in the row, false skips that data 
        #Ex: if you wanted to see if a column(series) has a certain value or its comparsion to that value
            #capitals['Percentage'] > 25 will return boolean statement on that comparison 
            # capitals[capitals['Percentage']] reutrns rows

#Watch assigning vlaues demo again  

