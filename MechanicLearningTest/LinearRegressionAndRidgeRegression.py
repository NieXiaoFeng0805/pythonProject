# @Time: 2022/7/15 16:38
# @Author: 丨枫
# @File LinearRegressionAndRidgeRegression.py
import re

import numpy as np
import matplotlib.pyplot as plt
import warnings

# 引入sklearn线性回归
from sklearn.linear_model import LinearRegression as LR  # 回归模型
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor, Ridge

plt.rcParams["font.family"] = "SimHei"  # 字体
plt.rcParams["axes.unicode_minus"] = False  # 正常显示正负号
plt.rcParams["font.size"] = 12  #
warnings.filterwarnings("ignore")  # 取消一般警告显示

# 导入数据
filename = "housing.data"
f = open(filename).readlines()  # 读取所有行
data = []
for i in f:
    raw_data = re.sub(r"\s{2,}", " ", i).strip()  # 将空格合并并去掉换行符号
    data.append(raw_data.split(" "))  # 数据以空格分开添加到列表中
data = np.array(data).astype(np.float_)  # 将数据转为矩阵，类型为float
# print(data[0:406, :])

Y = data[:, -1].reshape(506, 1)  # 将最后一列作为标签
X = data[:, 0:-1].reshape(506, 13)  # 前13列作为特征
# 设置训练集和测试集
X_train = X[0:406, :]
Y_train = Y[0:406, :]
X_test = X[406:, :]
Y_test = Y[406:, :]

# # sklearn线性回归
#
lr = LR().fit(X_train, Y_train)
y_hat0 = lr.predict(X_test)  # 预测
# print(y_hat0)
print(lr.score(X_train, Y_train))
print(lr.score(X_test, Y_test))
#
# 绘图
plt.subplot(2, 1, 1)
plt.title("由sklearn内置线性回归预测得到")
x_len = np.arange(len(X_test))
# plt.title("由sklearn内置线性回归预测得到")
plt.plot(x_len, Y_test, color='r', label='真实值')  # 真实值
plt.plot(x_len, y_hat0, color='g', label='预测值')  # 预测值
plt.legend()

# 脊回归：在原有的基础上增加了正则化项
# 因为原来的回归模型在特征值上没有偏差，所以在特征之间由关联的时候，最小二乘会有较大的噪声，解变得不稳定

# 数据标准化
transfer = StandardScaler()
X_train = transfer.fit_transform(X_train)
X_test = transfer.transform(X_test)
# print(X_train)
# print(X_test)

# 预估器
# 参数说明
# alpha正则化强度  100
est = Ridge(alpha=100, max_iter=10000, solver='sag')
e = est.fit(X_train, Y_train)
y_hat1 = e.predict(X_test)
print(e.score(X_train, Y_train))
print(e.score(X_test, Y_test))
# print(y_hat1)


# 绘图
x_len = np.arange(len(X_test))
plt.subplot(2, 1, 2)
plt.title("脊回归预测")
plt.plot(x_len, Y_test, color='r', label='真实值')  # 真实值
plt.plot(x_len, y_hat1, color='g', label='预测值')  # 预测值
plt.legend()
plt.show()
