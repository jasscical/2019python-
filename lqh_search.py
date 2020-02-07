# -*- coding: utf-8 -*-
import pandas as pd 
import os
import glob

os.getcwd()
os.chdir('I:\qqData')

def searchName(name):
    files=glob.glob('*.xlsx')
    
    for filename in files:
        print('\n')
        print(filename)
        
        df=pd.read_excel(filename,sheet_name= 'Sheet2',header =2)
        df1=df['姓名']
        print(df1)
        a=name in df1.values
        if(a):
            print("您要搜索的字符串为: ",name)
            print("搜索结果为：",filename)
            return 0
        
       
       

def testrun():
    searchName('lqh')
    
testrun()