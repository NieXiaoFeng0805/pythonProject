# @Time: 2022/6/30 17:54
# @Author: 丨枫
# @File SVMalgorithm.py
from sklearn import datasets  # 导入数据集
from sklearn.model_selection import train_test_split  # 划分数据集，随机划分训练集和测试集
from sklearn.preprocessing import StandardScaler  # 将数据进行归一化和标准化
from sklearn.svm import SVC  # 非线性多维支持向量分类
from matplotlib.colors import ListedColormap  # ListedColormap允许用户使用十六进制颜色码来定义自己所需的颜色库，并作为plt.scatter()中的cmap参数出现：
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore")  # 取消一般警告显示

iris = datasets.load_iris()
# print(iris.data)
X = iris.data[:, [2, 3]]  # 选第三列和第四列作为数据
# print(X)
y = iris.target  # 作为标签
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)  # 测试集占比30%，随机种子设为0

sc = StandardScaler()  # 数据进行归一化和标准化作为对象
# sc.fit_transform()
sc.fit(X_train)  # 对训练集进行拟合
X_train_std = sc.transform(X_train)  # 对训练集通过居中和缩放执行标准化
X_test_std: object = sc.transform(X_test)  # 同上

# 决策区域可视化
def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    # 设置marker generator和color map
    # 分类结果区别决策区域并可视化表示
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])  # y的种类有三种，不同种类用不同颜色标记
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1  # 取X矩阵的第0列的最小值-1、最大值+1，赋值x1_min, x1_max
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1  # X矩阵的第1列的最小值-1、最大值+1，赋值 x2_min, x2_max
    # 生成网格采点样
    # 构造向量，扩展成一个二维矩阵，resolution向量差值
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),  # 绘制xx1矩阵
                           np.arange(x2_min, x2_max, resolution))  # 绘制xx2矩阵

    # 还原成单位向量
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    # Z 表示分类后的数据模式

    # 数据化分类线
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim = (xx2.min(), xx2.max())
    X_test, y_test = X[test_idx, :], y[test_idx]
    for idx, cl in enumerate(np.unique(y)):  # np.unique:去除重复数据
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], alpha=0.8, c=cmap(idx), marker=markers[idx], label=cl)
    if test_idx:
        X_test, y_test = X[test_idx, :], y[test_idx]
        plt.scatter(X_test[:, 0], X_test[:, 1], c='black', alpha=0.8, linewidths=1, marker='o', s=10, label='test set')


# vstack 和 hstack 都是进行数据拼接； vstack要求相同列数、hstack要求相同行数
X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))
svm = SVC(kernel='linear', C=1.0, random_state=0)  # 使用线性核函数，设置C值为1
svm.fit(X_train_std, y_train) # 拟合
plot_decision_regions(X_combined_std, y_combined, classifier=svm, test_idx=range(105, 150))  # 调用函数
plt.xlabel('petal length {standardized}')
plt.ylabel('petal width {standardized}')
plt.legend(loc='upper left')
plt.show()
