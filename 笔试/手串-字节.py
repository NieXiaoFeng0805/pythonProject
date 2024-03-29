# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/15 18:02
# software: PyCharm
"""
文件说明：

"""
# 排列组合函数
import itertools
from scipy.special import comb, perm  # 组合、排列
import collections


# perm(3,2) ==6
# comb(3,2)==3

# 笛卡尔积 list(product(product_list, repeat=2))
# [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'c')]

# 排列  list(permutations(product_list, 2))
# [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]

# 组合（无重复） list(combinations(product_list, 2))
# [('a', 'b'), ('a', 'c'), ('b', 'c')]

# 组合（有重复） list(combinations_with_replacement(product_list, 2))
# [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]

# 手串颜色c种、手串长度为n、每个串珠包含的颜色已知(num[i] 表示第i颗珠子有多少种颜色）
# 要求
#   1. 在连续m个串珠里每个颜色至多出现一次
#   2. 1<=n<=10000; 1<=m<=1000; 1<=c<=50
#   3. 找出多少种颜色在任意连续m个串珠中至少出现了两次

class Solution:
    def create_num(self):
        # 几个串珠、要求连续m个、颜色共c种
        n, m, c = [int(x) for x in input().split()]
        target = []
        for i in range(n):
            target.append([int(x) for x in input().split()])
        return n, m, target

    def m_target(self, start, m, target):
        res = []
        for i in range(start, start + m):
            if target[i][0] != 0:
                res.extend(target[i][1:])
            else:
                pass
        return res

    def solution(self):
        n, m, target = self.create_num()
        target.append(target[0])  # 串起来
        start = 0
        res = []
        while start < n - m + 2:
            m_t = self.m_target(start, m, target)
            color_dict = collections.Counter(m_t)  # 存储颜色
            for k, v in color_dict.items():
                if v > 1 and k not in res:
                    res.append(k)
            start += 1
        print(len(res))


Solution().solution()
