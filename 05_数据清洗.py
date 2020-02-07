# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import missingno as mn
import matplotlib.pyplot as plt
from sklearn import preprocessing


def dealException():
    for num in range(6,9,1):
        print("now is work in---"+"HO_",num,".csv")
        
        #df=pd.read_csv("HO_{}.csv".format(str(num) ) )
        
        
        data_train=pd.read_csv("HO_{}.csv".format(str(num) ) )
        data_train['dates'] = pd.to_datetime(data_train['dates'])
        
        df = data_train.set_index('dates')
        

        year='2017'
        Month=df['month']
        Day=df['day']
        
        for i in range(8,27,1):
            date='2017-8-{}'.format(i)
            a=df[date]
            a=a['normal_time']
            print(a.head(20))
        
#        a=a.reset_index(drop = True)
#        columns=['arrive_time', 'normal_time']
#        a=a[columns]
#        print(a.head())
#       
##        a=a['dates']
##        
#        print(a.head())
  
        #a=df['2017-10'].max()
        
        
#        a=['2017-6-31'].isin(df.columns())
#        print(df)
        
#        print(df.isnull().sum())
#        df=df['normal_time']
        
        #cat_col=['normal_time']
        #dummies=pd.get_dummies(df[cat_col])
        #print(dummies.values=='NaN')
        
        #用列均值代替空值
#        for column in list(a.columns[a.isnull().sum() > 0]):
#            mean_val = a[column].mean()
#            a[column].fillna(mean_val, inplace=True)
#        print(a.isnull().sum())



        
# =============================================================================
         
 
          
# =============================================================================
#           for i in cat_col:
#                print (pd.Series(df[i]).value_counts())
#                plt.plot(df[i])
# =============================================================================
          #df=df.columns.values.tolist()
         
         
# =============================================================================
        #print(df.head(50))
        

# =============================================================================
#         mn.matrix(df)
#         df=df.dropna(thresh=df.shape[0]*0.5,axis=1)
#         print(df.head(10))
# =============================================================================





       
# =============================================================================
#         #replace_value = 0.0
# 	    #df = df.fillna(replace_value, inplace = True)
#         #df.fillna(replace_value,inplace=True)
# =============================================================================
        
        
# =============================================================================
#         total = df.isnull().sum().sort_values(ascending=False)
#         percent =(df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
#         missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
#         print(missing_data.head(20))      
#         print(total)
# =============================================================================
        
        
# =============================================================================
#         monthMin=Month.min()
#         monthMax=Month.max()
#         dayMin=Day.min()
#         dayMax=Day.max()
#         
#         for month in range(monthMin,monthMax+1,1):
#             for day in range(dayMin,dayMax+1,1):
#                 
#                 date=year+'-'+ str(month)+'-'+ str(day) 
#                 print(date)
#                 df=df[date]
#                 
#                 
#                 print(df.isna())
# =============================================================================
                
                
                


        
        
        
       
       
        
        
        
    
        
    

        
      
        
        
       
       
        
        
        




if __name__ == "__main__":
    dealException()
    

