#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from pandas import DataFrame
db=pd.read_csv('Desktop\My project\AYUSHHospitals.csv')
db.head()


# In[18]:


#db.head()
#db['Srl no.'].is_unique
#db.loc[3000]
#db.get_dtype_counts()
#plt.show()
# df = DataFrame(db,columns='State / UT',index = ['Govt. Hospitals','Local Body Hospitals','Other Hospitals'])
#df.plot(x='State / UT', y=index, kind='bar')


# In[35]:


import pandas as pd #importing pandas
import numpy as np #importing numpy
import matplotlib.pyplot as plt #importing matplotlib

from pandas import DataFrame #importing DataFrame from pandas
db=pd.read_csv('Desktop\My project\AYUSHHospitals.csv') #reading the bed datasheet

db.set_index('Srl no.', inplace=True) #setting 'Srl no.' column as the index

df = pd.DataFrame(db,columns=['State / UT','Total Hospitals','Total Beds']) #calling columns from 'Hospital' database

#(i) Calculating Ratio
df['Ratio']='NaN' #setting the declared column 
df['Ratio']=round(df['Total Beds']/df['Total Hospitals']) #calculating ratio of beds to hospitals and rounding off the result
df['Ratio']=df['Ratio'].replace(np.nan,0) #replacing all NaN values with 0
  
#df.sort_values('Ratio',ascending=False)
df.to_csv('Desktop\My project\HALOOOO.csv') #saving the full columns

#(ii) Finding out colums with max and minimum ratio.
print(df[df['Ratio']==df['Ratio'].max()])
print(df[df['Ratio']==df['Ratio'].min()])

#(iii) Plotting the data
#Plotting Ratio against State
x=df['State / UT'] #Take x-axis as State name
y=df['Ratio'] #Take y- axis as Ratio of Beds to Hospitals
plt.plot(x,y,label='linear') #plot x v/s y in a linear graph
plt.xticks(rotation=90) #To rotate x-axis values by 90 degree for better readability
plt.legend('Ratio') #Legend
plt.show() #Display the graph

#Plotting Hospitals against State
y1=df['Total Hospitals'] #Take y axis as Total Hospitals
plt.plot(x,y1,label='linear',color='green') #changing line color
plt.xticks(rotation=90)
plt.legend('Hospitals')
plt.show()

#Plotting Beds against State
y2=df['Total Beds'] #Take y-axis as Total Beds
plt.plot(x,y2,label='linear',color='red')
plt.xticks(rotation=90)
plt.legend('Beds')
plt.show()

#Plotting all values against State in one graph 
plt.plot(x,y,label='linear')
plt.plot(x,y1,label='linear',color='green')
plt.plot(x,y2,label='linear',color='red')
plt.xticks(rotation=90)
plt.legend('All')
plt.show()


# In[10]:


#db.head()
#df = pd.DataFrame(db,columns=['Srl no.','State / UT','Govt. Hospitals','Local Body Hospitals','Other Hospitals','Total Hospitals','Govt. Beds','Local Body Beds','Other Beds','Total Beds'])

#print(df[df['Ratio']==df['Ratio'].min() and df['Total Hospitals']==0 && df['Total Beds']==0])


# In[ ]:




