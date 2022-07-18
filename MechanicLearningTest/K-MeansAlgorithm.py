# @Time: 2022/7/13 19:51
# @Author: 丨枫
# @File K-MeansAlgorithm.py
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
import warnings

plt.rcParams["font.family"] = "SimHei"  # 字体
plt.rcParams["axes.unicode_minus"] = False  # 正常显示正负号
plt.rcParams["font.size"] = 12  #
warnings.filterwarnings("ignore")  # 取消一般警告显示

# 参数：
# n_samples=100  样本数量
# n_features=2   特征数量
# centers=3      中心点

# 返回值：
# X_train:  测试集
# y_train： 特征值

X_train, y_train = make_blobs(n_samples=100, n_features=2, centers=3)
# 描绘数据图
plt.figure(0)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
plt.title('数据集图')



# 参数说明
# n_clusters  将预测结果分为几簇
kmeans = KMeans(n_clusters=3)  # 获取模型并设定簇的总数
kmeans.fit(X_train)  # 用K-Means算法进行拟合

# 使用数据进行预测
y_ = kmeans.predict(X_train)
plt.figure(1)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train)  # 预测结果
plt.figure(2)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_)  # 原结果
plt.show()