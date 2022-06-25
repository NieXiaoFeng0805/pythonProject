import random
import math

x = int(input('扔飞镖的次数：'))
count = 0
for i in range(0, x):
    a = random.uniform(-1, 1)  # 随机浮点数，random()不支持-1 1
    b = random.uniform(-1, 1)
    if a ** 2 + b ** 2 <= 1:
        count += 1
Pi = (count / float(x)) * 4
print('Pi 的估计值为:', Pi)
