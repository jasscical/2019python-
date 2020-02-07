import glob
import pandas as pd
import codecs 
import os

os.getcwd()
os.chdir('I:/Anacoda3/AcondaProject/Haikou_Order/all2')

def txtmerge():
    files = glob.glob('*.txt')
    all = codecs.open('allOrder.txt','a')
    
    for filename in files:
        print("now is merging:"+filename)
        fopen = codecs.open(filename,'r',encoding='utf-8')
        lines=[]
        lines = fopen.readlines()
        fopen.close()       
        for line in lines:
            for x in line:
                all.write(x)
                
        all1 = pd.read_csv('allOrder.txt',sep='\t',low_memory=False)
        
        all1.to_csv('all2.csv')
        print(filename+"   is finished")
    print('work over')
    return 0
        
if __name__ == '__main__':
    txtmerge()