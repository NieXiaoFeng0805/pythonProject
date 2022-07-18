# @Time: 2022/7/16 15:03
# @Author: 丨枫
# @File PredictHousingPrice.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from sklearn.model_selection import train_test_split  # 划分数据集，随机划分训练集和测试集

plt.rcParams["font.family"] = "SimHei"  # 字体
plt.rcParams["axes.unicode_minus"] = False  # 正常显示正负号
plt.rcParams["font.size"] = 12  #
warnings.filterwarnings("ignore")  # 取消一般警告显示


# 引入代价函数J(θ)
def CostFunction(X, y, theta):
    inners = np.power(((X * theta.T) - y), 2)  # 计算误差；（θT*X - y）^2
    return np.sum(inners) / (2 * len(X))  # 返回总误差，(1/2m)∑inners


# 梯度下降函数
def gradientDensent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))  # 设置零矩阵，其维度与θ矩阵维度相同
    p = theta.shape[1]  # 参数的个数
    cost = np.zeros(iters)  # 保存迭代后的cost
    for i in range(iters):
        error = (X * theta.T) - y  # 计算误差
        for j in range(p):  # 同时更新参数
            term = np.multiply(error, X[:, j])  # 计算其内积
            temp[0, j] = theta[0, j] - ((alpha / len(X)) * np.sum(term))  # 计算更新参数θ
        theta = temp  # 将更新后的参数覆盖原参数值
        cost[i] = CostFunction(X, y, theta)  # 调用代价函数计算新误差
    return theta, cost  # 返回更新值


# 正规方程法
def normalEqn(X, Y):
    theta = np.linalg.inv(X.T @ X) @ X.T @ Y  # X.T@X等价于X.T.dot(X)
    return theta


# 导入数据
filepath = "ex1data2.txt"  # 文件路径
# 参数说明  文件路径    去除文件头   赋予列名
raw_data = pd.read_csv(filepath, header=None, names=['houseSize', 'Roomnumber', 'Prices'])
# print(raw_data.head())  # 测试前5条数据，看是否正常

# 进行归一化处理，因为量级差距过大会导致梯度下降过慢
data = (raw_data - raw_data.mean()) / raw_data.std()  # 样本数据减去其平均值再除以标准差
# print(data.head())

# 加入偏置(常数项b)
data.insert(0, 'Ones', 1)  # 第0列加入一列为1 的常数数
# print(data.head())

# 划分测试集和训练集
# print(data.shape[1])  # 获取列数  shape[0]获取维度
cols = data.shape[1]
# 划分特征与标签
X = data.iloc[:, 0:cols - 1]  # 特征
Y = data.iloc[:, cols - 1:cols]  # 标签
# print(X.head())
# print(Y.head())

# 转成matrix格式
X = np.matrix(X.values)
Y = np.matrix(Y.values)
# print(X)
# print(Y)
# 初始化参数θ
theta = np.matrix(np.array([0, 0, 0]))
# 拆分数据集
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=40)
# print(x_train)
# print(y_train)
# 运行梯度下降算法
alpha = 0.03  # 学习率设定
iters = 10000  # 迭代次数设定
new_theta, cost = gradientDensent(X, Y, theta, alpha, iters)
print(new_theta)
# 正规方程法
finalTheta = normalEqn(X, Y)
print(finalTheta.T)
