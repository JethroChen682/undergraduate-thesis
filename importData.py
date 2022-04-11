import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def GenerateData(df):
    return df['5']-df['4']
file_path = r"/Users/chen/Documents/毕业论文/cities_yearbooks_2000-2018/"
file1 = "200"
file3 = "城市年鉴.xlsx"
df = pd.read_excel(file_path+file1+str(0)+file3, sheet_name='1')
df.set_index('Unnamed: 0',inplace=True)
colomuns=df.columns
df=df.loc[df['Unnamed: 1'].notnull()&df.index.notnull(),:]
df.dropna(axis=0,how='any',inplace=True)
m1=df.dtypes


dictionary = {'3':[1,None,3],'5':[1,2,3],'4':[1,2,3]}
m=pd.DataFrame(dictionary)
m['1433223'] =m.apply(GenerateData,axis=1)
mm=m['1433223'].value_counts()
m.loc[:,'3']=m['3'].fillna(method='bfill')
df2=pd.read_excel(r"/Users/chen/Documents/2022软微成绩.xlsx",sheet_name="Sheet1",skiprows=2)
df2.dropna(axis=1,how='all',inplace=True)
# m.to_excel(file_path+"test1.xlsx",index=False)
mm3=slice(3)
a=1