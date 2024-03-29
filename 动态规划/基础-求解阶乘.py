# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/18 15:56
# software: PyCharm
"""
文件说明：

"""


class Fact:

    def fact(self, n: int):
        '''
        求解阶乘————递归实现
        :param n:
        :return:
        '''
        if n < 1:
            return 1
        # return Fact(n - 1) * n if n > 0 else 1
        return fact(n - 1) * n

    def FactByDP(self, n: int):
        '''
        求解阶乘————动态规划实现_递归
        通过设置一个数组来记录当前计算状态，实现状态转移
        :param n:
        :return:
        '''
        dp = [-1] * (n + 1)

        def fact(n):
            if dp[n] == -1:  # 之前没计算过的状态
                dp[n] = fact(n - 1) * n if n > 0 else 1
            return dp[n]  # 之前已经计算过这个状态，直接返回

        fact(n)


Fact().FactByDP(6)
