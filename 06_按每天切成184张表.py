import pandas as pd
import os




def splitByDay():
    for num in range(1,9,1):
        print("now is working in---"+"HO_",num,".csv")
        print('\n')
        
        #df=pd.read_csv("HO_{}.csv".format(str(num) ) )
        
        
        data_train=pd.read_csv("I:\Anacoda3\AcondaProject\dataOfOrderAnalysis\HO_{}.csv".format(str(num) ) )
        data_train['dates'] = pd.to_datetime(data_train['dates'])
        
        df = data_train.set_index('dates')
        
        year='2017'
        Month=df['month']
        Day=df['day']
        
        monthMin=Month.min()
        monthMax=Month.max()
        dayMin=Day.min()
        dayMax=Day.max()
        spl(df,year,monthMin,monthMax,dayMin,dayMax)
        
        
        
        
        
def spl(df,year,monthMin,monthMax,dayMin,dayMax):
    
    df=df
    year=year
    monthMin=monthMin
    monthMax=monthMax
    dayMin=dayMin
    dayMax=dayMax
        

    for month in range(monthMin,monthMax+1,1):
        if month==6 or month==9:
            dayMax=30
        for day in range(dayMin,dayMax+1,1):
            date=year+'-'+ str(month)+'-'+ str(day)
            #date='2017-8-{}'.format( str( day))
            print(date)
            a=df[date]
            print('\n')                              
            for column in list(a.columns[a.isnull().sum() > 0]):
                mean_val = a[column].mean()
                a[column].fillna(mean_val, inplace=True)
            #I:\Anacoda3\AcondaProject\dataOfOrderAnalysis\subList\
            a=a.reset_index(drop = True)
            columns=['type','start_dest_distance', 'arrive_time', 'departure_time', 'pre_total_fee', 'normal_time']
            a=a[columns]
            
            filename = '{}.csv'.format( str(date) )
            print('now is split  --- '+filename )
            
            mergeOrJustWrite(a,filename)
            #a.to_csv(filename)
            print('save   '+filename+' over!' ) 
            print('\n')


    
            
            
            
def mergeOrJustWrite(a,filenameBeChecked):
    a=a
    samefilename=filenameBeChecked
    
    #path='I:/Anacoda3/AcondaProject/dataOfOrderAnalysis/subList'
    path='I:/Anacoda3/AcondaProject/dataOfOrderAnalysis/subList/tomysqlFinished'
    #os.getcwd()
    #os.chdir(path)
    
    files = file_name(path)
    
#    for fname in files:
#        print(fname)

    
    if str(samefilename) in files:
        print(samefilename+' already exist!')
        a.to_csv('{}/re/{}'.format( path,str( samefilename)))
        #os.chdir(path)
      
    else:
        print('a new file!')
        a.to_csv('{}/{}'.format( path,str ( samefilename)))
        
    
      
def file_name(file_dir): 
    for root, dirs, files in os.walk(file_dir):
        return files
        #print(root) #当前目录路径  
        #print(dirs) #当前路径下所有子目录  
        #print(files) #当前路径下所有非目录子文件  
        

             
      
       
        
        
        
    
        
    

        
      
        
        
       
       
        
        
        




if __name__ == "__main__":
    splitByDay()
    



