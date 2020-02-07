import pandas as pd

def modifyCols(Pre,num):
    Pre=Pre
    num=num
    print(Pre)
    df=pd.read_csv('I:\Anacoda3\AcondaProject\Haikou_Order\{}.txt'.format(str(Pre)),
                   sep='\t')
    #'{}.'.format(str(Pre))
    df.rename(columns={'{}.order_id'.format(str(Pre)):'order_id',
                       '{}.product_id'.format(str(Pre)):'product_id',
                      '{}.city_id'.format(str(Pre)):'city_id',
                      
                       '{}.district'.format(str(Pre)):'district',
                       '{}.county'.format(str(Pre)):'county',
                       '{}.type'.format(str(Pre)):'type',
                       
                       '{}.combo_type'.format(str(Pre)):'combo_type',
                       '{}.traffic_type'.format(str(Pre)):'traffic_type',
                       '{}.passenger_count'.format(str(Pre)):'passenger_count',
                       
                       '{}.driver_product_id'.format(str(Pre)):'driver_product_id',
                      '{}.start_dest_distance'.format(str(Pre)):'start_dest_distance',
                      '{}.arrive_time'.format(str(Pre)):'arrive_time',
                      
                      '{}.departure_time'.format(str(Pre)):'departure_time',
                      '{}.pre_total_fee'.format(str(Pre)):'pre_total_fee',
                      '{}.normal_time'.format(str(Pre)):'normal_time',
                      
                     '{}.product_1level'.format(str(Pre)):'product_1level',
                     '{}.dest_lng'.format(str(Pre)):'dest_lng',
                     '{}.dest_lat'.format(str(Pre)):'dest_lat',
                     
                     '{}.starting_lng'.format(str(Pre)):'starting_lng',
                      '{}.starting_lat'.format(str(Pre)):'starting_lat',
                      '{}.bubble_trace_id'.format(str(Pre)):'bubble_trace_id',
                      '{}.year'.format(str(Pre)):'year',
                      '{}.month'.format(str(Pre)):'month',
                      '{}.day'.format(str(Pre)):'day',
                       },inplace=True)
    print("modifying columns......")
    cols=df.columns.values.tolist()
    print(cols)
    df=df.to_csv("HO_{}.csv".format(str(num)),index=False)
    
    

def Pre(prefix):
    return prefix

def Num(num):
    return num

def run():
    for i in range(8,9,1):
        num=Num(i)
        pre=Pre("dwv_order_make_haikou_{}".format(str(num)))
        modifyCols(pre,num)
        print(pre+"modify columns success!")
   

if __name__=="__main__":
    run()