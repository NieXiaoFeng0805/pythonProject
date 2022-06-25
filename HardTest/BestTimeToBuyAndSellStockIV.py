# @Time: 2022/6/11 10:35
# @Author: 丨枫
# @File BestTimeToBuyAndSellStockIV.py
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0 or len(prices) == 0:
            return 0
        # 在III的基础上可知，只有完成交易的情况才有可能获得利益，所以完成k次交易则利润最大化
        cost = [-prices[0]] * k  # 初始化完成k次交易的花费状态
        profit = [0] * k  # 初始化所有完成k次的利润状态
        for i in range(1, len(prices)):
            for count in range(k):  # 记录状态
                if count == 0:  # 初始状态
                    cost[count] = max(cost[count], -prices[i])  # 初始花费
                else:
                    cost[count] = max(cost[count], profit[count - 1] - prices[i])
                profit[count] = max(profit[count], cost[count] + prices[i])  # 计算利润
                # print(profit[count])
        print(profit)
        return profit[k - 2]


if __name__ == '__main__':
    Test = Solution()
    k, prices = 2, [2, 4, 1]
    Test.maxProfit(k, prices)
