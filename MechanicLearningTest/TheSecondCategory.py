# @Time: 2022/6/25 23:01
# @Author: 丨枫
# @File TheSecondCategory.py
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression  # 调用逻辑回归
from sklearn.model_selection import train_test_split  # 划分数据集，即将原始数据分为训练集和测试集两部分
from sklearn.datasets import load_iris  # 调用Iris数据集
import warnings

plt.rcParams["font.family"] = "SimHei"  # 字体
plt.rcParams["axes.unicode_minus"] = False  # 正常显示正负号
plt.rcParams["font.size"] = 12  #

warnings.filterwarnings("ignore")  # 取消一般警告显示
# 数据集里一共包括150行记录，其中前四列为花萼长度，花萼宽度，花瓣长度，花瓣宽度等4个用于识别鸢尾花的属性，第5列为鸢尾花的类别
iris = load_iris()  # 引用Iris数据集
# data为训练所需的数据集，target为数据集对应的分类标签
X, y = iris.data, iris.target
# print(X)
# print(y)
# 因为鸢尾花具有三个类别，4个特征，此处仅使用其中两个特征，并且移除一个类别(类别0)
X = X[y != 0, 2:]  # 取标签值不为0且采用第三和第四个特征
y = y[y != 0]  # 标签值采用不为零的类别
# print("x=", X)
# print("y=", y)

# 此时，y的标签为1与2,这里将其改成0与1，(仅仅足为了习惯而已)
y[y == 1] = 0
y[y == 2] = 1

# 将数据集分为训练集（x_train，y_train）和测试集（X_test，y_test）两部分；其中
# test_size表示测试集大小，即测试集所占整个数据集的比例，默认0.25
# random_state 随机数种子，为复现结果设置，随机状态不同结果就不同


# 但这个为什么会影响预测结果呢？明明数据集是不变的测试集比例和训练集比例也是不变的，random_state是指分割方法随机吗？
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=40)

lr = LogisticRegression()
lr.fit(X_train, y_train)  # 进行拟合
y_hat = lr.predict(X_test)  # 用测试集进行预测
# print(y_hat)
# print("权重: ", lr.coef_)
# print("偏置: ", lr.intercept_)
# print("真实值:", y_test)
# print("预测值:", y_hat)

# 绘图

# 两种类别
c1 = X[y == 0]
c2 = X[y == 1]

# 将两种鸢尾花的数据可视化
plt.scatter(x=c1[:, 0], y=c1[:, 1], c="g", label="类别0")  # 将属0类别的鸢尾花的两种特征属性存入，用绿色标识
plt.scatter(x=c2[:, 0], y=c2[:, 1], c="r", label="类别1")  # 将属1类别的鸢尾花的两种特征属性存入，用红色标识
plt.xlabel("花瓣长度")  # x轴
plt.ylabel("花瓣宽度")  # y轴
plt.title("鸢尾花样本分布")  # 图标题
plt.figure(1)
plt.plot()
plt.legend()  # 在图上显示数据标签

# 绘制预测结果与真实结果
# 参数说明：绘制内容、绘制形状、绘图线种类-默认实线、大小、颜色、标签等
plt.figure(2)
plt.plot(y_test, marker='o', ls='', ms=15, c='r', label='真实类别')  # 数据集中的测试集，用于结果即真实类别
plt.plot(y_hat, marker='x', ls='', ms=15, c='g', label='预测类别')  # 预测结果
plt.xlabel('样本序号')
plt.ylabel('类别')
plt.title('逻辑回归分类预测结果')
plt.legend()
plt.plot()
plt.show()
