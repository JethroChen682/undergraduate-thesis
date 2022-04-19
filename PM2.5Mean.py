import pandas as pd
file='PM2.5Data.xlsx'
df=pd.read_excel(file)
df.set_index(['城市'],inplace=True)
index=df.index
set=set()
for x in index:
    set.add(x)
df1=pd.DataFrame(columns=df.columns)
for city in set:
    data=df.loc[city, :]
    bool=data.size!=9
    if bool:
        mean=pd.DataFrame(df.loc[city, :].mean(axis=0)).T
        mean.index=[city]
        df1=pd.concat([df1,mean],axis=0)
    else:
        temp=pd.DataFrame(df.loc[city,:]).T
        temp.index=[city]
        df1=pd.concat([df1,temp],axis=0)
df1.dropna(axis=0,inplace=True,how='any')
m=df1.describe()
# df1.to_excel('PM2.5.xlsx')

