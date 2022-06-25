# @Time: 2022/6/8 10:05
# @Author: 丨枫
# @File BestTimeToBuyAndSellStockII.py
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # 一次只能买入一股且只能在这股抛出后才能买入下一股
        # 所以还是计算与下一天的收益并取累加即可
        profit = 0  # 初始利润
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:  # 收益为正
                profit += (prices[i] - prices[i - 1])
        print(profit)


if __name__ == '__main__':
    Test = Solution()
    prices = [1, 2, 3, 4, 5]
    Test.maxProfit(prices)
