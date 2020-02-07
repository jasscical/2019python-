# -*- coding: utf-8 -*-
import pandas as pd
import os


def DropCols():
    file_dir='I:\Anacoda3\AcondaProject\dataOfOrderAnalysis\subList'   
    files=file_name(file_dir) 
    for fname in files:
        print(fname)
        df=pd.read_csv("{}.csv".format(str(fname) ) )
        
        x=[0]
        df.drop(df.columns[x],axis=1,inplace=True)
        
        print('save start---')
       
        #date_1[['mobile', 'plan_id']].to_csv(output_file, sep=',', header=True,index=False)
        df=df.to_csv("{}.csv".format( str( fname)))
        print('save end')
 
        



        

def file_name(file_dir): 
    for root, dirs, files in os.walk(file_dir):
        return files      
 
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
