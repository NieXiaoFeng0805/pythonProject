# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/18 17:05
# software: PyCharm
"""
文件说明：
一次可以跳上 1 级台阶，也能跳上 2 级台阶
求跳上一个n级台阶有多少种跳法（答案对 10^9+7取模）
注： n=0 时， 结果为1 ; n=1时，结果为1

例子： n=7 结果：21
"""


class Solution:
    def solution(self, n):
        dp = [-1] * (n + 1)
        dp[0] = 1  # 初始状态
        dp[1] = 1

        for i in range(2, n + 1):
            # 状态转移方程
            dp[i] = dp[i - 1] + dp[i - 2]  # 即跳上i阶的方案数 = 跳上 i-1 阶的方案数 + 跳上 i-2 阶的方案数
            dp[i] = dp[i] % (10 ^ 9 + 7)

        return dp[n]  # 返回跳上 n 阶的方案数


Solution().solution(7)
