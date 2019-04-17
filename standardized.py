# -*- coding:utf-8 -*-
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

inputfile = './data/business_circle.xls'
outputfile = './data/standardized.xls'

# 加载数据
data = pd.read_excel(inputfile, index_col='基站编号')
# print(data.head(5))
# print(data.info())

# 离差标准化
mm = MinMaxScaler()
data = pd.DataFrame(mm.fit_transform(data.values), index=data.index, columns=data.columns)
data = data.reset_index()
print(data.head(10))

data.to_excel(outputfile, index=False)