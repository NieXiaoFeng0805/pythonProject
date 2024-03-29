# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/18 16:42
# software: PyCharm
"""
文件说明：

"""


class Solution:
    def Fib_ByRecur(self, n: int):
        '''
        计算斐波那契数列
        设 F[]为状态数组，
        状态转移方程为： F[i] = F[i-1] + F[i-2]
        F[0]=0
        F[1]=1
        :param n:
        :return:
        '''
        dp = [-1] * (n + 1)  # 状态数组
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp  # 前n项斐波那契数列
        # return dp[n-1] # 第n项斐波那契数列


Solution().Fib_ByRecur(6)
