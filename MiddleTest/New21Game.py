# @Time: 2022/7/18 10:45
# @Author: 丨枫
# @File New21Game.py
import numpy as np


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # 不是很理解题目的意思
        """
        # 每次抽取是独立的，即每张牌的概率为1/maxPts
        # 当得分大于等于k时停止

        Pts_sum = 0  # 累计得分
        while Pts_sum < k:  # 累计得分大于等于k值跳出循环
            random_num = np.random.randint(1, maxPts + 1)  # 随机 1-maxPts的数
            Pts_sum += random_num
        # print(Pts_sum)
        # 要求小于等于n的概率即为 在区间[k，Pts_sum] 内的数小于等于n的概率
        molecular = len(range(k, n + 1))  # 分子
        denominator = len(range(0, Pts_sum))  # 分母
        if molecular >= denominator:
            return 1.0
        print(molecular / denominator)
        return molecular / denominator"""

        # 大佬解法
        # 假设 dp[x] 为她手上牌面为x时，能获胜的概率，那么这个概率应该是：
        # dp[x] = 1 / w * (dp[x + 1] + dp[x + 2] + dp[x + 3]... + dp[x + w])
        # 因为抽取的牌面机会都是均等的，她能抽取的面值在[1, maxPts]之间，所以将概率之和平均一下就是dp[x]的概率。
        dp = [0] * (k + maxPts)
        Pts_sum = 0  # 计算累加牌面
        for i in range(k, k + maxPts):  # 此时已不能抽卡，计算不大于n的概率
            dp[i] = 1 if i <= n else 0
            Pts_sum += dp[i]
        for j in range(k - 1, -1, -1):  # 能抽卡时，计算每种不大于n的牌面的可能性
            dp[j] = Pts_sum / maxPts
            Pts_sum = Pts_sum - dp[j + maxPts] + dp[j]  # 从后往前计算概率的和
        return dp[0]


if __name__ == '__main__':
    Test = Solution()
    n, k, maxPts = 6, 1, 10
    Test.new21Game(n, k, maxPts)
