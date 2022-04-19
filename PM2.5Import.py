import pandas as pd
import os
file_path=r'/Users/chen/Documents/毕业论文/PM2.5/站点_20210101-20211231'
file1='china_sites_20210126.csv'
df1=pd.read_csv(os.path.join(file_path,file1))
columns=df1.columns
dtypes=df1.dtypes
df1=df1.loc[df1['hour']==100000,:]
df1=df1.loc[df1['hour']==100000,:]
m=os.listdir(file_path)
for fileName in os.listdir(file_path):
     file=os.path.join(file_path,fileName)
     if file[-1]!='e':
         df2=pd.read_csv(file)
         if df2.iloc[0,0]!='<head><title>404 Not Found</title></head>':
             df2 = df2.loc[(df2['hour'] == 12) & (df2['type'] == 'PM2.5_24h'), :]
             df1=pd.concat([df1,df2],ignore_index=True)
df3=df1.mean(axis=0)
df3.to_excel('2021.xlsx')