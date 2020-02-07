# -*- coding: utf-8 -*-
import pandas as pd
import os
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="I:\Anacoda3\AcondaProject\Haikou_Order"):
    #返回文件的路径
    return os.path.join(base_dir,"{}.csv".format(str(symbol)))

def get_data1(symbols,dates):
    df = pd.DataFrame(index = dates)
    
    for symbol in symbols:
        df_temp=pd.read_csv(symbol_to_path(symbol),index_col='county',sep='\t',
                             usecols=['dwv_order_make_haikou_1.departure_time'],parse_dates=True)
        #df_temp=df_temp.rename(columns = {'departure_time':symbol})
        df = df.join(df_temp)
        df = df.dropna()
    #注意这个return的位置，别放在循环里了！！！    
    return df
 
    def get_data2(symbols,dates):
    df = pd.DataFrame(index = dates)
    
    for symbol in symbols:
        df_temp=pd.read_csv(symbol_to_path(symbol),index_col='county',sep='\t',
                             usecols=['dwv_order_make_haikou_5.departure_time'],parse_dates=True)
        #df_temp=df_temp.rename(columns = {'departure_time':symbol})
        df = df.join(df_temp)
        df = df.dropna()
    #注意这个return的位置，别放在循环里了！！！    
    return df
def plot_data(df,title='count of depature_time'):
    a=df.plot(title=title,fontsize=12)
    a.set_xlabel("Date",fontsize=12)
    a.set_ylabel("count",fontsize=12)
    plt.show()

#归一化，使图像更加清晰（在0~n之间）
def normalize(df):
    return df/df.ix[0,:]

      
def test_run():
    symbols1 = ['all1']
    symbols2 = ['all2']
    dates=pd.date_range('2017-05-01','2017-10-31')   
    df1 = get_data1(symbols1,dates)
    df2 = get_data2(symbols1,dates)
    print(df1)
    print(df2)
    #plot_data(df)
 
test_run()

