# -*- coding: utf-8 -*-
import pandas as pd
import os
import re

def delete_error_date():
# =============================================================================
#    # path = 'I:/Anacoda3/AcondaProject/dataOfOrderAnalysis/subList'
#    # dates_filesname = file_name(path)
#       for date_fname in dates_filesname:
#         print(date_fname)
#         datelist=re.findall(r'(.+?)\.', date_fname)
#         date=str(datelist[0])
# =============================================================================
    year='2017'
    dayMax=31
    
    for month in range(5,11,1):
        if month==6 or month==9:
            dayMax=30          
        for day in range(1,dayMax+1,1):  
            month_open=month
            month_date=month
            date_open=year+'-'+str( month_open)+'-'+ str(day)
            print('date_open : '+date_open)
            df=pd.read_csv("I:/Anacoda3/AcondaProject/dataOfOrderAnalysis/subList/{}.csv".format(str(date_open)))
            #选取包含当前日期的数据
            if month_date<10:
                month_date='0'+str(month_date)
            if day<10:
                day='0'+str(day)
            date=year+'-'+str( month_date)+'-'+ str(day)   
            df=df[df['departure_time'].str.contains(date)]
            df=df[df['arrive_time'].str.contains(date)]
            
            #print(df.head(500))
            
            #normal_time,start_dest_distance :求平均值，大于15%或者小于15%的删掉
            #逻辑：1.先删除normal_time,start_dext_distance里面的含空值的行
            #2.再求平均值
            #3.把df写入源文件保存
            
            #实现1
            df=df.dropna(axis=0, how='all')
            #print(df.head(500))
            
            #实现2
            mean_normal_time = df['normal_time'].mean()
            mean_start_dest_distance = df['start_dest_distance'].mean()
      
            mean_normal_time_low_15 = mean_normal_time*0.85
            mean_normal_time_up_15 = mean_normal_time*1.15            
            mean_start_dest_distance_low_15 = mean_start_dest_distance*0.85
            mean_start_dest_distance_up_15 = mean_start_dest_distance*1.15
            
            df=df.loc[(df['normal_time'].astype(float) >  mean_normal_time_low_15) &
                  (df['normal_time'].astype(float) < mean_normal_time_up_15),:]
           # print(df['normal_time'])
            
            df=df.loc[(df['start_dest_distance'].astype(float) >  mean_start_dest_distance_low_15) &
                  (df['start_dest_distance'].astype(float) < mean_start_dest_distance_up_15),:]
            
            #print(df['start_dest_distance'])
            #筛选之后数据变少了
            #print(df)
            
            df=df.drop('Unnamed: 0',1)
            print('start save----'+ str(date))
            df.to_csv('I:/Anacoda3/AcondaProject/dataOfOrderAnalysis/subList/dataClear/{}.csv'.format(str (date)) ,index=False)
            print( str(date)+' save over!!!!')
            print('\n')
    
# =============================================================================
# def file_name(file_dir): 
#     for root, dirs, files in os.walk(file_dir):
#         return files
#         #print(files) #当前路径下所有非目录子文件  
#         #print(root) #当前目录路径  
#         #print(dirs) #当前路径下所有子目录  
#        
# =============================================================================



if __name__ == '__main__':
    #date='2017-05-01'
    delete_error_date()