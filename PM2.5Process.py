import pandas as pd
import os
df=pd.DataFrame()
for i in range(15,22):
    year='20'+str(i)
    file_name=year+'.xlsx'
    dfTemp=pd.read_excel(file_name,skiprows=2)
    dfTemp.columns=['cityCode',year]
    dfTemp.set_index(['cityCode'],inplace=True)
    df=pd.concat([df, dfTemp], axis=1)
fileSite='站点列表-2022.02.13起.xlsx'
dfSite=pd.read_excel(fileSite)
dfSite.set_index(['监测点编码'], inplace=True)
df=pd.concat([df,dfSite],axis=1)
df.to_excel('PM2.5Data.xlsx')