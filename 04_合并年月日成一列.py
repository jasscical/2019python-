# -*- coding: utf-8 -*-

import pandas as pd


def mergeCols():
    for num in range(2,9,1):
        print("now is merging columns in---"+"HO_",num,".csv")
        df=pd.read_csv("HO_{}.csv".format(str(num) ) )
        
        #parent_teacher_data['address'] = parent_teacher_data['country']+parent_teacher_data['province']+parent_teacher_data['city']+parent_teacher_data['county']
        df['dates']= df['year'].map(str) +'-'+ df['month'].map(str)+'-'+df['day'].map(str)
        print('test start')
       
        
        df=df.to_csv("HO_{}.csv".format(str(num)))
        print('test end')
        
       
 
def GetCols():
     for num in range(1,2,1):
        print("now is showing---",num)
        df=pd.read_csv("HO_{}.csv".format(str(num) ) )
        cols=df.columns.values.tolist()
        print(cols)
        
#        a=df
#        columns=['arrive_time', 'normal_time']
#        a=a[columns]
#        print(a.head())
        
        #df=df.head(3)
        
        #df=df.ix[1:2]
        
        
       
       

    
if __name__ =="__main__":
    #mergeCols()
    GetCols()