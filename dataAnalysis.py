#西北地区城市空气污染对人口迁移的影响
import pandas as pd
cityList=['西安市','兰州市','西宁市','银川市','乌鲁木齐市']
# file_path = r"/Users/chen/Documents/毕业论文/年鉴/中国城市年鉴1994-2020/中国城市统计年鉴地级市面板数据（99-2019）.xlsx"
file_path = r"/Users/chen/Documents/毕业论文/年鉴/中国城市年鉴1994-2020/中国城市统计年鉴地级市面板数据（99-2019）.xlsx"

df = pd.read_excel(file_path, sheet_name='Sheet1',skiprows=1)
columns=df.columns
dtype=df.dtypes
df=df.loc[df['城市'].isin(cityList),:]
df.to_excel('DataCity.xlsx')
a=1