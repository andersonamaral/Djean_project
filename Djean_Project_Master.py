
# coding: utf-8

# ### ETL Aggregating by Country to Djean Axt Swiss Company
# ### Author : Anderson Amaral , email : luis.anderson.sp@gmail.com 
# ### LinkedIn: https://www.linkedin.com/in/andersonlamaral/
# 

# In[46]:

import pandas as pd


# Below I read the Excel file into a Pandas DataFrame. Realise I have delete manually the first 3 columns in order to Pandas read correctly the file. If it always happen like that, I can add some stuff to always delete these 3 rows automatically
# 
# Obs: *At the same time I am reading a file, I am also calling it df *

# In[47]:

df = pd.read_excel('/home/anderson/Desktop/Djean_project/ander.xlsx', sheetname='WorldWide Tickets', header=0)


# Now , let's gonna check the first 5 rows in order to see if everything is ok.

# In[48]:

df.head(5)


# First, we should see how many different countries we have on this file :

# In[49]:

df['Country'].unique()


# In[50]:

numbercountries = df['Country'].nunique()
print("We have",numbercountries,"different countries")


# Now, let's gonna check some details of the dataframe "df"

# In[51]:

df.info()


# Now, I am gonna create a for loop to generate dataframes based on the countries names! That will be very handy for the user (my friend, by the way)!!

# In[52]:

d = {}
for name in df['Country']:
    d[name] = df[df['Country'] == name]

Very nice the for loop above, isn't? Let's see if it works, by calling any country.Below I will be calling Brazil then later France, the first  3 rows of each new dataframe I just made for every country using th for loop aforementioned :
# In[53]:

d['Brazil'].head(3)


# In[54]:

d['France'].head(3)


# It works!! Now, I just need to make every dataframe turn into a Excel file or csv file!!
# 

# Here I have picked up 5 countries which dataframe are going to be printed as csv into the folder "Countries"

# In[55]:

d['Brazil'].to_csv('/home/anderson/Desktop/Djean_project/Countries/Brazil.csv' ,sep=';',index=False, encoding='utf-8')


# In[64]:

d['France'].to_csv('/home/anderson/Desktop/Djean_project/Countries/France.csv' ,sep=';',index=False, encoding='utf-8')


# In[65]:

d['Italy'].to_csv('/home/anderson/Desktop/Djean_project/Countries/Italy.csv' ,sep=';',index=False, encoding='utf-8')


# In[67]:

d['Switzerland'].to_csv('/home/anderson/Desktop/Djean_project/Countries/Switzerland.csv' ,sep=';',index=False, encoding='utf-8')


# "Now, you just need to copy and paste the same code above, for every country of you interest, and automatically a dataframe will be generate everytime you run this file"

# In[ ]:



