# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

filepath = './data/standardized.xls'
data = pd.read_excel(filepath, index_col='基站编号')

# scipy 层次聚类函数
Z = linkage(data, method='ward', metric='euclidean')    # 谱系聚类图
P = dendrogram(Z, 0)    # 画谱系聚类图
plt.show()