# @Time: 2022/8/26 15:00
# @Author: 丨枫
# @File SVM implementation.py

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from sklearn import svm
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split  # 划分数据集，即将原始数据分为训练集和测试集两部分
from sklearn.datasets import load_iris  # 调用Iris数据集
import warnings

plt.rcParams["font.family"] = "SimHei"  # 字体
plt.rcParams["axes.unicode_minus"] = False  # 正常显示正负号
plt.rcParams["font.size"] = 12  #

warnings.filterwarnings("ignore")  # 取消一般警告显示


# 定义分类器
def classifier():
    clf = svm.SVC(C=0.5,  # 惩罚项系数
                  kernel='linear',  # 线性核函数(高斯核)
                  decision_function_shape='ovr')  # 决策函数
    return clf


# 模型评估
def show_accuracy(a, b, tip):
    # acc = a.ravel() == b.ravel() 中会生成一个矩阵acc，其中每个元素都是True 或False
    # 而np.mean(acc) 则会计算出这个矩阵的均值，也就是正确率。
    acc = a.ravel() == b.ravel()
    print('%s 准确率:%.3f' % (tip, np.mean(acc)))


def print_accuracy(clf, X_train, y_train, X_test, y_test):
    # 分别打印训练集和测试集的准确率
    print('训练集预测率:%.3f' % (clf.score(X_train, y_train)))
    print('测试集预测率:%.3f' % (clf.score(X_test, y_test)))
    # 原始结果与预测结果进行对比
    show_accuracy(clf.predict(X_train), y_train, 'training data')
    show_accuracy(clf.predict(X_test), y_test, 'testing data')
    # 计算决策函数的值，表示x到各分割平面的距离
    print('decision_function:\n', clf.decision_function(X_train))


# 绘图（在两个特征的情况下）
def drawFigures(clf, x):
    iris_feature = '花萼长度', '花萼宽度', '花瓣长度', '花瓣宽度'
    x1_min, x1_max = x[:, 0].min(), x[:, 0].max()  # 第0列的范围
    x2_min, x2_max = x[:, 1].min(), x[:, 1].max()  # 第1列的范围

    x1, x2 = np.mgrid[x1_min:x1_max:200j, x2_min:x2_max:200j]  # 生成网格采样点
    grid_test = np.stack((x1.flat, x2.flat), axis=1)  # 测试点

    grid_hat = clf.predict(grid_test)  # 预测分类值 得到【0,0.。。。2,2,2】
    grid_hat = grid_hat.reshape(x1.shape)  # reshape grid_hat和x1形状一致

    # 设置颜色
    cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
    cm_dark = mpl.colors.ListedColormap(['g', 'b', 'r'])

    plt.pcolormesh(x1, x2, grid_hat, cmap=cm_light)  # 预测值的显示
    plt.scatter(x[:, 0], x[:, 1], c=np.squeeze(y), edgecolor='k', s=30, cmap=cm_dark)  # 样本点
    plt.scatter(X_test[:, 0], X_test[:, 1], s=30, facecolor='none', zorder=10)  # 测试点
    plt.xlabel(iris_feature[2], fontsize=13)
    plt.ylabel(iris_feature[3], fontsize=13)
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)

    plt.title("SVM对鸢尾花分类")
    plt.show()


iris = load_iris()  # 引用Iris数据集
# print(iris.data[0:5], iris.target[0:5])
# iris.data中即为鸢尾花的四个特征[花萼长度，花萼宽度，花瓣长度，花瓣宽度]，iris.target中为鸢尾花的分类
X = iris.data[:, 2:]  # 特征矩阵,选取花瓣长度和宽度作为特征进行分类，(四个特征不好绘图)
y = iris.target  # 标签矩阵
# print(X[0:5])
# 数据集的划分,将3成划为测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# print(X_train[:5], y[:5])

# 训练数据
svm_op = classifier()  # 获取SVM对象
svm_op.fit(X_train, y_train.ravel(), sample_weight=None)  # 开始拟合，(将测试集展成1维)
# print_accuracy(svm_op, X_train, y_train, X_train, y_test)  # 模型评估

# 绘图（在两个特征的情况下）
drawFigures(svm_op, X)
