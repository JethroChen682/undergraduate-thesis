import os
import pandas as pd
f1='PM2.5.xlsx'
f2='data.xlsx'
df1=pd.read_excel(f1)
df2=pd.read_excel(f2)
df2.set_index(['城市','年份'],inplace=True)
df=pd.DataFrame()
for year in range(2015,2020):
    yy=str(year)
    df3=df1[['城市',yy,'经度','纬度']]
    df3=df3.rename(columns={yy:'PM2.5'})
    df3.insert(df3.shape[1], '年份', year)
    df3.set_index(['城市','年份'],inplace=True)
    df=pd.concat([df,df3],axis=0)
df2=pd.concat([df2,df],axis=1)
df2.reset_index(inplace=True)
df2.dropna(axis=0,inplace=True,how='any')
df2.to_excel('ultimateData.xlsx')