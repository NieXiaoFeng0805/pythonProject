# @Time: 2022/7/18 23:26
# @Author: 丨枫
# @File ClassificationModelByMyself.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from scipy.io import loadmat  # 导入mat包需要
from scipy.optimize import minimize
from sklearn.metrics import classification_report  # 导入评价报告


# 激活函数
def Sigmoid(z):  # sigmoid函数
    return 1 / (1 + np.exp(-z))


def LeaklyReLU(z):  # leakly ReLU 函数
    return max(z, 0.01*z)


def tanh(z):  # 双曲正切函数
    return (np.exp(z) - np.exp(-z)) / (np.exp(z) + np.exp(-z))


# 代价函数
def CostFunction(theta, X, y, alpha):
    theta = np.matrix(theta)  # 转为矩阵格式
    X = np.matrix(X)
    y = np.matrix(y)
    first_part = np.multiply(-y, np.log(Sigmoid(X * theta.T)))  # 代价函数的第一部分
    second_part = np.multiply((1 - y), np.log(1 - Sigmoid(X * theta.T)))  # 代价函数的第二部分
    reg = (alpha / (2 * len(X))) * np.sum(np.power(theta[:, 1:theta.shape[1]], 2))  # 正则化项
    return np.sum(first_part - second_part) / len(X) + reg


# 梯度下降（向量化）
def gradientDensent(theta, X, y, alpha):
    theta = np.matrix(theta)  # 转为矩阵格式
    X = np.matrix(X)
    y = np.matrix(y)
    theta_nums = int(theta.ravel().shape[1])  # 将theta拉成一维数组再计算其列数，即需要更新的theta的个数
    errors = Sigmoid(X * theta.T) - y  # 计算误差
    grad = ((X.T * errors) / len(X)).T + ((alpha / len(X)) * theta)  # 计算梯度
    # 将截距的梯度正则化,即j=0时无需正则化
    grad[0, 0] = np.sum(np.multiply(errors, X[:, 0])) / len(X)
    return np.array(grad).ravel()


# 构建分类器
def Classifier(X, y, label_nums, alpha):
    rows = X.shape[0]  # 维度
    cols = X.shape[1]  # 参数个数
    # 为每个分类器构建参数
    all_theta = np.zeros((label_nums, cols + 1))  # +1个偏置
    # 第一列插入一列全1方便运算
    X = np.insert(X, 0, values=np.ones(rows), axis=1)
    # 将下标值从 1 开始，更好理解
    for i in range(1, label_nums + 1):
        theta = np.zeros(cols + 1)  # cols+1维向量，即为一组逻辑回归的参数
        y_i = np.array([1 if label == i else 0 for label in y])
        y_i = np.reshape(y_i, (rows, 1))  # 转为列向量

        # 最小化代价函数，寻找参数并传入准确正确位置
        fmin = minimize(fun=CostFunction, x0=theta, args=(X, y_i, alpha), method='TNC', jac=gradientDensent)
        all_theta[i - 1, :] = fmin.x
    return all_theta


# 预测
def PredictFunction(X, all_theta):
    rows = X.shape[0]  # 维度
    cols = X.shape[1]  # 参数个数
    label_nums = all_theta.shape[0]  # 标签数
    # 第一列插入一列全1方便运算
    X = np.insert(X, 0, values=np.ones(rows), axis=1)
    # 转成matrix格式
    X = np.matrix(X)
    all_theta = np.matrix(all_theta)
    h = Sigmoid(X * all_theta.T)
    h_max = np.argmax(h, axis=1)  # 取h矩阵中每行最大值
    h_max = h_max + 1  # 标签范围变成 1-10
    return h_max


data = loadmat('ex3data1.mat')  # 导入数据
# print(data)
# print(data['X'].shape, data['y'].shape)

# 随机取出100个
sample_idx = np.random.choice(np.arange(data['X'].shape[0]), 100)
sample_images = data['X'][sample_idx, :]
# print(sample_images)

# 绘出数据图
fig, ax = plt.subplots(nrows=10, ncols=10, sharey=True, sharex=True, figsize=(12, 12))
for row in range(10):
    for col in range(10):
        ax[row, col].matshow(np.array(sample_images[10 * row + col].reshape((20, 20))).T, cmap=matplotlib.cm.binary)
        plt.xticks(np.array([]))
        plt.yticks(np.array([]))
# plt.show()

# 保证维度准确
"""row = data['X'].shape[0]
col = data['X'].shape[1]
all_theta = np.zeros((10, col + 1))
X = np.insert(data['X'], 0, values=np.zeros(row), axis=1)
theta = np.zeros(col + 1)
y_0 = np.array([1 if label == 0 else 0 for label in data['y']])
print(y_0)
y_0 = np.reshape(y_0, (row, 1))
# print(X.shape, y_0.shape, theta.shape, all_theta.shape)

label = np.unique(data['y'])  # 标签数目
# print(label)
# print(data['y'])

# # 开始训练
all_theta = Classifier(data['X'], data['y'], 10, 1)  # 更新参数θ
print(all_theta)"""


# 训练
all_theta = Classifier(data['X'], data['y'], 10, 1)
print(all_theta)

# 预测
y_pred = PredictFunction(data['X'], all_theta)  # predict_all返回的预测值n*1的向量
correct = [1 if a == b else 0 for (a, b) in zip(y_pred, data['y'])]     # 判断预测值和标签是否相同
accuracy = (sum(map(int, correct)) / float(len(correct)))   # 计算预测正确率，就是correct中1的个数
print('accuracy = {0}%'.format(accuracy * 100))
