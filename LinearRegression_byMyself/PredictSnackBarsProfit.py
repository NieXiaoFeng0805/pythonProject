# @Time: 2022/7/5 22:59
# @Author: 丨枫
# @File PredictSnackBarsProfit.py
from IPython.core.pylabtools import figsize
from matplotlib import pyplot as plt
import warnings
import numpy as np
# numpy适用于处理“干净”的数据，及规范、无缺失的数据，而pandas更加擅长数据清洗(data munging)，这为后一步数据处理扫清障碍。
import pandas as pd

plt.rcParams["font.family"] = "SimHei"  # 字体
plt.rcParams["axes.unicode_minus"] = False  # 正常显示正负号
plt.rcParams["font.size"] = 12  #

warnings.filterwarnings("ignore")  # 取消一般警告显示


# 引入代价函数J(θ)
def CostFunction(X, y, theta):
    inners = np.power(((X * theta.T) - y), 2)  # 计算误差；（θT*X - y）^2
    return np.sum(inners) / (2 * len(X))  # 返回总误差，(1/2m)∑inners


# 进行梯度下降算法
# 参数说明  特征矩阵、输出、参数矩阵、学习率、迭代次数
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


# 读入数据
datapath = "ex1data1.txt"
# 读入数据并给数据标识，第一列为人口数量，第二列为开店利润
data = pd.read_csv(datapath, header=None, names=['people', 'profit'])
# print(data)
# 描绘数据散点图
# data.plot(kind='scatter', x='people', y='profit')
# plt.show()
# 注意到假设函数h(x) = θo+θ1*x；所以需要添加一列为1的数据
data.insert(0, 'ZeroCol', 1)
cols = data.shape[1]  # 1取列数、0取行数 即cols=3
# 用第几行第几列进行筛选。
X = data.iloc[:, :-1]  # X是data里的除最后列
y = data.iloc[:, cols - 1:cols]  # y是data最后一列
# print(X)
# print(data)
# 转为矩阵
X = np.matrix(X.values)
y = np.matrix(y.values)

# 设置学习率和迭代次数
alpha, iters = 0.01, 1500
theta = np.matrix(np.array([1, 1]))  # θ值初始化
# 调用梯度下降来训练数据
newTheta, cost = gradientDensent(X, y, theta, alpha, iters)

# 设置x的范围
x = np.linspace(data.people.min(), data.people.max(), 100)
# 假设函数
f = newTheta[0, 0] + newTheta[0, 1] * x
# 绘图
# 数据分布图
fig, ax = plt.subplots(figsize=(12, 8))
ax.scatter(data.people, data.profit)
ax.set_xlabel('人口')
ax.set_ylabel('小吃店利润')
ax.set_title('数据分布图')
# plt.show()

# 假设函数拟合图
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(x, f, 'r')
ax.scatter(data.people, data.profit)
ax.set_xlabel('人口')
ax.set_ylabel('小吃店利润')
ax.set_title('假设函数拟合图')
# plt.show()

# 代价函数的迭代图
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(np.arange(iters), cost, 'b')
ax.set_xlabel('迭代次数')
ax.set_ylabel('误差')
ax.set_title('代价函数的迭代图')
plt.show()
