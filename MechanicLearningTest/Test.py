# @Time: 2022/6/25 22:44
# @Author: 丨枫
# @File Test.py
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "SimHei"  # 字体
plt.rcParams["axes.unicode_minus"] = False  # 正常显示正负号
plt.rcParams["font.size"] = 12  # 字号


# 定义sigmoid函数。
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


z = np.linspace(-10, 10, 200)
plt.plot(z, sigmoid(z))
# 绘制水平线与垂直线。
plt.axvline(x=0, ls="-", c="k")  # 在x=0处整一条竖线
plt.axhline(ls=":", c="k")  # y=0处一条水平虚线
plt.axhline(y=0.5, ls=":", c="k")  # y=0.5处
plt.axhline(y=1, ls=":", c="k")  # y=1处
plt.xlabel("z值")  # x轴
plt.ylabel("sigmoid(z)值")  # y轴
plt.show()  # 显示
