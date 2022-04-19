import os
import pandas as pd
file='PopulationData.xlsx'
df=pd.read_excel(file)
df.dropna(axis=0,inplace=True,how='any')
df=df.loc[~df['城市'].str.contains('省|自治区')]
df=df.loc[(df['年份']>2014),:]
df.to_excel('data.xlsx')
# year='2019'
# filePath=r'/Users/chen/Documents/毕业论文/各年数据'
# file=os.path.join(filePath,'2014_2019.xlsx')
# df=pd.read_excel(file)
# # df.dropna(axis=0,inplace=True,how='any')
# df=df.loc[(df['年份']<=2019)&(df['年份']>=2014),:]
# df.to_excel('PopulationData.xlsx')
# foo=os.path.join(filePath,year)
# fileList=os.listdir(foo)
# df=pd.DataFrame()
# for file in fileList:
#     if file!='.DS_Store':
#         fileP=os.path.join(foo,file)
#         df1=pd.read_excel(fileP)
#         df1.dropna(axis=0,inplace=True,how='any')
#         df1=df1.loc[df1.iloc[:,0]!='城 市',:]
#         df1.set_index(['城 市'],inplace=True)
#         df=pd.concat([df,df1],axis=1)
# df.dropna(axis=0,inplace=True,how='any')
# df.to_excel('2019.xlsx')
# for i in range(2014,2021):
#     os.makedirs(filePath+r'/'+str(i))