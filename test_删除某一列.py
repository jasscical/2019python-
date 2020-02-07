# -*- coding: utf-8 -*-
import pandas as pd

def showCols(df):
    df_col=df.columns.values.tolist()
    print(df_col)
    
def dropCol():
    df=pd.read_csv("test.csv")
    print(df)
    df=df.drop('c',1)
    df.to_csv('test.txt')
    print(df)
    
def searchCol():
    df=pd.read_csv("test.txt")
    c=df['a'].values.tolist()
    print(c)
    
    
    
    

if __name__=="__main__":
    #dropCol()
    searchCol()