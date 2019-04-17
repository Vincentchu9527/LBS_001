# -*- coding:utf-8 -*-
import pandas as pd
from sklearn.cluster import AgglomerativeClustering     # sklearn中的层次聚类函数
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

filepath = './data/standardized.xls'
k = 3 # 聚类数

data = pd.read_excel(filepath, index_col='基站编号')
model = AgglomerativeClustering(n_clusters=k, linkage='ward')
model.fit(data)

# 详细输出原始数据及其类别
r = pd.concat([data, pd.Series(model.labels_, index=data.index, name='聚类类别')], axis=1)
print(r.head(10))

# 画图
style = ['ro-', 'bo-', 'go-']

for i in range(k):
    plt.figure()
    tmp = r[r['聚类类别'] == i].iloc[:, :4]
    for j in range(len(tmp)):
        plt.plot(range(1, 5), tmp.iloc[j], style[i])

    plt.title('商圈类别' + str(i+1), fontsize=20)
    plt.xticks(range(1, 5), data.columns, rotation=20)
    plt.subplots_adjust(bottom = .18)   # 调整底部, 让标签显示完全
    plt.show()