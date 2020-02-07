# -*- coding: utf-8 -*-
import pandas as pd
import os

def file_name(file_dir): 
    for root, dirs, files in os.walk(file_dir):
        return files
        #print(root) #当前目录路径  
        #print(dirs) #当前路径下所有子目录  
        #print(files) #当前路径下所有非目录子文件  
        
def appendSameFile():
    pathFrom='I:/Anacoda3/AcondaProject/dataOfOrderAnalysis/subList/re'
    pathTo='I:/Anacoda3/AcondaProject/dataOfOrderAnalysis/subList'
    filesFrom=file_name(pathFrom)
    filesTo=file_name(pathTo)
    
    for fr in filesFrom:    
        if str(fr) in filesTo:
            print('same file is---'+fr)
            df=pd.read_csv('{}/{}'.format( str(pathFrom), str( fr)))
            
            print('append start......')
            df.to_csv('{}/{}'.format( str(pathTo), str( fr)), mode='a+',header=False,index=False)
            print('append ok!')
            
            print('\n')
        
        

if __name__ =='__main__':
    appendSameFile()