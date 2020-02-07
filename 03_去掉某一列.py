# -*- coding: utf-8 -*-
import pandas as pd


def DropCols():
    for num in range(1,2,1):
        print("now is dropping columns in---"+"HO_",num,".csv")
        df=pd.read_csv("HO_{}.csv".format(str(num) ) )
        
        #df=df.drop['Unnamed: 0',1]
        
        x=[0]
        df.drop(df.columns[x],axis=1,inplace=True)
        
        print('save start---')
       
        #date_1[['mobile', 'plan_id']].to_csv(output_file, sep=',', header=True,index=False)
        df=df.to_csv("HO_{}.csv".format(str(num)))
        print('save end')
        
       
 
def GetCols():
     for num in range(8,9,1):
        print("now is showing---",num)
        df=pd.read_csv("HO_{}.csv".format(str(num) ) )
        cols=df.columns.values.tolist()       
        #cols=df.columns[0]
        print(cols)
        print(df)
       
       

    
if __name__ =="__main__":
    #DropCols()
    GetCols()