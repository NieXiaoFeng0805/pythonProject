# @Time: 2022/6/25 23:01
# @Author: 丨枫
# @File TheSecondCategory.py
from sklearn.linear_model import LogisticRegression #逻辑回归
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import warnings

warnings.filterwarnings("ignore")

iris = load_iris()
X, y = iris.data, iris.target
# 因为或尾花具有三个类别，4个特征，此处仅使用其中两个特征，并且移除一个类别(类别0)
X = X[y != 0, 2:]
y = y[y != 0]
# 此时，y的标签为1与2,我们这里将其改成0与1，(仅仅足为了习惯而已)
y[y == 1] = 0
y[y == 2] = 1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2)
lr = LogisticRegression()
lr.fit(X_train, y_train)
y_hat = lr.predict(X_test)
print("权重: ", lr.coef_)
print("偏置: ", lr.intercept_)
print("真实值: ", y_test)
print("预测值:", y_hat)
