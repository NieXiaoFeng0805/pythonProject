# @Time: 2022/7/16 15:03
# @Author: 丨枫
# @File PredictHousingPrice.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from sklearn.model_selection import train_test_split  # 划分数据集，随机划分训练集和测试集

from LinearRegression_byMyself.PredictSnackBarsProfit import cost

plt.rcParams["font.family"] = "SimHei"  # 字体
plt.rcParams["axes.unicode_minus"] = False  # 正常显示正负号
plt.rcParams["font.size"] = 12  #
warnings.filterwarnings("ignore")  # 取消一般警告显示


# 引入代价函数J(θ)
def CostFunction(X, y, theta):
    inners = np.power(((X * theta.T) - y), 2)  # 计算误差；（θT*X - y）^2
    # inners = np.power((np.dot(X, (theta.T)) - y, 2))  # 向量法
    return np.sum(inners) / (2 * len(X))  # 返回总误差，(1/2m)∑inners


# 梯度下降函数
def gradientDensent(X, y, theta, alpha, iters):
    # 一般解法
    """
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
    return theta, cost  # 返回更新值"""
    # 向量解法
    cur_cost = np.zeros((1, iters))  # 存储每个样本的代价，为向量形式
    for i in range(iters):
        cur_cost[0, i] = CostFunction(X, y, theta)  # 计算每个样本代价
        inners = np.dot(X, (theta.T)) - y  # 计算偏差
        temp = np.dot(inners.T, X)
        theta = theta - alpha * temp / m  # 更新θ
    return theta, cur_cost


# 正规方程法
def normalEqn(X, Y):
    theta = np.linalg.inv(X.T @ X) @ X.T @ Y  # X.T@X等价于X.T.dot(X)
    cost = CostFunction(X, Y, theta.T)
    return theta, cost


# 绘图
def drawFigures(iters, cost_list):
    fig, ax = plt.subplots(figsize=(12, 8))  # 一张图，其大小为12*8
    ax.plot(iters, cost_list[0], 'r', label='alpha=0.01')
    ax.plot(iters, cost_list[1], 'g', label='alpha=0.03')
    ax.plot(iters, cost_list[0], 'b', label='alpha=0.09')
    ax.plot(iters, cost_list[0], 'y', label='alpha=0.1')
    ax.plot(iters, cost_list[0], 'pink', label='alpha=0.3')
    ax.plot(iters, cost_list[0], '*r', label='alpha=0.6')
    ax.plot(iters, cost_list[0], '*b', label='alpha=0.9')
    ax.legend(loc=2)
    ax.set_xlabel('迭代次数')
    ax.set_ylabel('下降速度')
    ax.set_title('不同学习率其下降速度随迭代次数的变化图')
    plt.show()


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
theta = np.zeros((1, X.shape[1]))
# 拆分数据集
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=40)
# print(x_train)
# print(y_train)
# 运行梯度下降算法
m = X.shape[0]  # 样本数
alpha = np.array([0.01, 0.03, 0.09, 0.1, 0.3, 0.6, 0.9])  # 学习率设定
iters = 50  # 迭代次数设定
# 用cost_list存储不同学习率下的每次迭代后的代价，
cost_list = np.zeros((len(alpha), iters))
for i in range(len(alpha)):  # 学习率取不同值
    cur_theta, cur_cost = gradientDensent(X, Y, theta, alpha[i], iters)
    cost_list[i] = cur_cost
# 绘制不同学习率其下降速度随迭代次数的变化图
drawFigures(np.arange(iters), cost_list)

# new_theta, cost = gradientDensent(X, Y, theta, alpha, iters)
# print(new_theta, cost)
# # 正规方程法
# finalTheta = normalEqn(X, Y)
# print(finalTheta.T)
