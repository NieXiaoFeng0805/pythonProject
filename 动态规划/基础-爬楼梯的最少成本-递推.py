# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/18 18:29
# software: PyCharm
"""
文件说明：
数组的每个下标作为一个阶梯，第i个阶梯对应一个非负数的体力花费 cost[i]
支付体力值可以选择向上爬 一个 或 两个 阶梯
求：爬到顶的最低花费
注：可以选择下标为0或1 的作为初始阶梯

例： cost= [10,15,20]
输出  15 最低，花费15从 cost[1]开始到顶刚好2步
"""


class Solution:
    def solution(self, cost_list):
        n = len(cost_list)
        dp = [-1] * (n + 1)  # dp[i] 表示到达i层的最小花费
        # 初始状态，可以选择下标0或1的元素作为起始阶梯
        dp[0], dp[1] = 0, 0

        for i in range(2, n+1):
            # 到达第 i 个 阶梯， 是到达i-1层的最小花费 + 从它向上爬的花费 和 i-2层的最小花费 + 从它向上爬的花费；
            # 二者去小值
            dp[i] = min(dp[i - 1] + cost_list[i - 1], dp[i - 2] + cost_list[i - 2])
        return dp[n]  # 返回到顶端的最小花费


Solution().solution([12, 15, 20])
