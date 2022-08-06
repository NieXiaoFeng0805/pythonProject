# @Time: 2022/8/1 21:49
# @Author: 丨枫
# @File BPNetWork.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from scipy.io import loadmat
from sklearn.preprocessing import OneHotEncoder
from scipy.optimize import minimize
from sklearn.metrics import classification_report  # 评价报告


# 用sigmoid函数作为激活函数
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# 前向传播
def forwardPropagate(X, theta1, theta2):
    m = X.shape[0]  # 数据维度
    # 一共就两层，计算两次a和z即可
    a1 = np.insert(X, 0, values=np.ones(m), axis=1)  # 插入一列全为0的数方便计算，输入层
    # 隐藏层
    z2 = a1 * theta1.T
    a2 = np.insert(sigmoid(z2), 0, values=np.ones(m), axis=1)
    # 输出层
    z3 = a2 * theta2.T
    h = sigmoid(z3)

    return a1, z2, a2, z3, h


# 代价函数
def costFunction(theta1, theta2, input_size, hidden_size, num_labels, X, y, learning_rate):
    m = X.shape[0]  # 获得数据维度
    # 转换成矩阵格式
    X = np.matrix(X)
    y = np.matrix(y)

    # 运行前向传播
    a1, z2, a2, z3, h = forwardPropagate(X, theta1, theta2)

    # 计算代价
    J = 0
    for i in range(m):
        first_term = np.multiply(-y[i, :], np.log(h[i, :]))  # 代价函数的第一部分
        second_term = np.multiply((1 - y[i, :]), np.log(1 - h[i, :]))  # 代价函数的第二部分
        J += np.sum(first_term - second_term)  # 相加

    J = J / m

    return J


# 正则化
def costReg(theta1, theta2, input_size, hidden_size, num_labels, X, y, learning_rate):
    m = X.shape[0]
    X = np.matrix(X)
    y = np.matrix(y)

    # 运行前向传播
    a1, z2, a2, z3, h = forwardPropagate(X, theta1, theta2)

    # 计算代价
    J = 0
    for i in range(m):
        first_term = np.multiply(-y[i, :], np.log(h[i, :]))
        second_term = np.multiply((1 - y[i, :]), np.log(1 - h[i, :]))
        J += np.sum(first_term - second_term)

    J = J / m

    # 加入正则项
    J += (float(learning_rate) / (2 * m)) * (np.sum(np.power(theta1[:, 1:], 2)) + np.sum(np.power(theta2[:, 1:], 2)))

    return J


# sigmoid 函数的梯度
def sigmoid_gradient(z):
    return np.multiply(sigmoid(z), (1 - sigmoid(z)))


# 反向传播
def backprop(params, input_size, hidden_size, num_labels, X, y, learning_rate, theta1, theta2):
    m = X.shape[0]
    X = np.matrix(X)
    y = np.matrix(y)

    # 运行前向传播
    a1, z2, a2, z3, h = forwardPropagate(X, theta1, theta2)

    # reshape the parameter array into parameter matrices for each layer
    # 更新每层的参数
    theta1 = np.matrix(np.reshape(params[:hidden_size * (input_size + 1)], (hidden_size, (input_size + 1))))
    theta2 = np.matrix(np.reshape(params[hidden_size * (input_size + 1):], (num_labels, (hidden_size + 1))))

    # 初始化
    J = 0
    delta1 = np.zeros(theta1.shape)  # (25, 401)
    delta2 = np.zeros(theta2.shape)  # (10, 26)

    # 计算代价
    for i in range(m):
        first_term = np.multiply(-y[i, :], np.log(h[i, :]))
        second_term = np.multiply((1 - y[i, :]), np.log(1 - h[i, :]))
        J += np.sum(first_term - second_term)

    J = J / m

    # perform backpropagation
    # 开始反向传播
    for t in range(m):
        a1t = a1[t, :]  # (1, 401)
        z2t = z2[t, :]  # (1, 25)
        a2t = a2[t, :]  # (1, 26)
        ht = h[t, :]  # (1, 10)
        yt = y[t, :]  # (1, 10)

        d3t = ht - yt  # (1, 10)

        z2t = np.insert(z2t, 0, values=np.ones(1))  # (1, 26)
        d2t = np.multiply((theta2.T * d3t.T).T, sigmoid_gradient(z2t))  # (1, 26)

        delta1 = delta1 + (d2t[:, 1:]).T * a1t
        delta2 = delta2 + d3t.T * a2t

    delta1 = delta1 / m
    delta2 = delta2 / m

    return J, delta1, delta2


# 加入正则项的反向传播
def backpropReg(params, input_size, hidden_size, num_labels, X, y, learning_rate):
    m = X.shape[0]
    X = np.matrix(X)
    y = np.matrix(y)

    # reshape the parameter array into parameter matrices for each layer
    # 更新参数
    theta1 = np.matrix(np.reshape(params[:hidden_size * (input_size + 1)], (hidden_size, (input_size + 1))))
    theta2 = np.matrix(np.reshape(params[hidden_size * (input_size + 1):], (num_labels, (hidden_size + 1))))

    # 运行前向传播
    a1, z2, a2, z3, h = forwardPropagate(X, theta1, theta2)

    # 初始化代价和参数
    J = 0
    delta1 = np.zeros(theta1.shape)  # (25, 401)
    delta2 = np.zeros(theta2.shape)  # (10, 26)

    # 计算代价
    for i in range(m):
        first_term = np.multiply(-y[i, :], np.log(h[i, :]))
        second_term = np.multiply((1 - y[i, :]), np.log(1 - h[i, :]))
        J += np.sum(first_term - second_term)

    J = J / m

    # add the cost regularization term
    J += (float(learning_rate) / (2 * m)) * (np.sum(np.power(theta1[:, 1:], 2)) + np.sum(np.power(theta2[:, 1:], 2)))

    # perform backpropagation
    for t in range(m):
        a1t = a1[t, :]  # (1, 401)
        z2t = z2[t, :]  # (1, 25)
        a2t = a2[t, :]  # (1, 26)
        ht = h[t, :]  # (1, 10)
        yt = y[t, :]  # (1, 10)

        d3t = ht - yt  # (1, 10)

        z2t = np.insert(z2t, 0, values=np.ones(1))  # (1, 26)
        d2t = np.multiply((theta2.T * d3t.T).T, sigmoid_gradient(z2t))  # (1, 26)

        delta1 = delta1 + (d2t[:, 1:]).T * a1t
        delta2 = delta2 + d3t.T * a2t

    delta1 = delta1 / m
    delta2 = delta2 / m

    # add the gradient regularization term
    delta1[:, 1:] = delta1[:, 1:] + (theta1[:, 1:] * learning_rate) / m
    delta2[:, 1:] = delta2[:, 1:] + (theta2[:, 1:] * learning_rate) / m

    # unravel the gradient matrices into a single array
    grad = np.concatenate((np.ravel(delta1), np.ravel(delta2)))

    return J, grad


# 导入数据
raw_data = loadmat('C:/Users/FBI OPENTHDOOR/Desktop/数据集/BP神经网络数据集/ex4data1.mat')
# print(raw_data)

# 分数据和标签
X = raw_data['X']  # 数据
y = raw_data['y']  # 标签
# print(X.shape, y.shape)

# 导入权重
weight = loadmat('C:/Users/FBI OPENTHDOOR/Desktop/数据集/BP神经网络数据集/ex4weights.mat')
# 将权重赋予参数向量
theta1, theta2 = weight['Theta1'], weight['Theta2']
# print(theta1.shape, theta2.shape)

# 待分类数据图
"""
sample_idx = np.random.choice(np.arange(raw_data['X'].shape[0]), 100)
sample_images = raw_data['X'][sample_idx, :]
fig, ax_array = plt.subplots(nrows=10, ncols=10, sharey=True, sharex=True, figsize=(12, 12))
for r in range(10):
    for c in range(10):
        ax_array[r, c].matshow(np.array(sample_images[10 * r + c].reshape((20, 20))).T, cmap=matplotlib.cm.binary)
        plt.xticks(np.array([]))
        plt.yticks(np.array([]))
plt.show()
"""

encoder = OneHotEncoder(sparse=False)  # 分类编码变量，将每一个类可能取值的特征变换为二进制特征向量，每一类的特征向量只有一个地方是1，其余位置都是0
# 即先进行拟合在进行标准化
y_onehot = encoder.fit_transform(y)  # 将其适用与标签，将（5000，1）变为（5000，10）
# print(y_onehot.shape)
# print(y[0], y_onehot[0,:])


# 初始化设置
input_size = 400  # 输入大小
hidden_size = 25  # 隐藏层单元数量
num_labels = 10  # 标签数量
learning_rate = 1  # 学习率

# 调用代价函数
cost1 = costFunction(theta1, theta2, input_size, hidden_size, num_labels, X, y_onehot, learning_rate)
cost2 = costReg(theta1, theta2, input_size, hidden_size, num_labels, X, y_onehot, learning_rate)
# print(cost1, cost2)

# np.random.random(size) 返回size大小的0-1随机浮点数，即随机参数初始值
params = (np.random.random(size=hidden_size * (input_size + 1) + num_labels * (hidden_size + 1)) - 0.5) * 0.24

# minimize the objective function
# 计算参数最优解
fmin = minimize(fun=backpropReg, x0=(params), args=(input_size, hidden_size, num_labels, X, y_onehot, learning_rate),
                method='TNC', jac=True, options={'maxiter': 250})
# print(fmin)

# 转格式
X = np.matrix(X)
thetafinal1 = np.matrix(np.reshape(fmin.x[:hidden_size * (input_size + 1)], (hidden_size, (input_size + 1))))
thetafinal2 = np.matrix(np.reshape(fmin.x[hidden_size * (input_size + 1):], (num_labels, (hidden_size + 1))))

# 计算使用优化后的θ得出的预测
a1, z2, a2, z3, h = forwardPropagate(X, thetafinal1, thetafinal2)
y_pred = np.array(np.argmax(h, axis=1) + 1)

# 预测值与实际值比较

print(classification_report(y, y_pred))

# 可视化隐藏层
"""
hidden_layer = thetafinal1[:, 1:]
fig, ax_array = plt.subplots(nrows=5, ncols=5, sharey=True, sharex=True, figsize=(12, 12))
for r in range(5):
    for c in range(5):
        ax_array[r, c].matshow(np.array(hidden_layer[5 * r + c].reshape((20, 20))), cmap=matplotlib.cm.binary)
        plt.xticks(np.array([]))
        plt.yticks(np.array([]))
"""
