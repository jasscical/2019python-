# -*- coding: utf-8 -*-
import os
import pandas as pd


if __name__ =='__main__':
    dir = 'I:\Anacoda3\AcondaProject\dataOfOrderAnalysis\subList'
    file_list = os.listdir(dir)
    for i in range(len(file_list)):
        print('第'+str(i)+'个表')
        print('\n')
        file_path = os.path.join(dir, file_list[i])
        if os.path.isfile(file_path):
            df=pd.read_csv(file_path)
            