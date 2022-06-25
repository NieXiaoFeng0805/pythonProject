# @Time: 2022/4/29 15:03
# @Author: 丨枫
# @File 最佳买入时机.py
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        # 初始利润
        minProfit = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            # 比较每天的利润并找到最大值
            maxProfit = max(maxProfit, prices[i] - minProfit)
            minProfit = min(minProfit, prices[i])
        print(maxProfit)
        return maxProfit


if __name__ == '__main__':
    Test = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    # prices = [2, 1, 4]
    Test.maxProfit(prices)
