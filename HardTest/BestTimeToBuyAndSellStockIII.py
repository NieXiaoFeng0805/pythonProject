# @Time: 2022/6/8 17:21
# @Author: 丨枫
# @File BestTimeToBuyAndSellStockIII.py
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # # 与II不同的是，只有两次购买与售出的机会，所以不能以每天的利润相加进行计算
        # # 设置次数count=2；每找到一次利润最大时将count减一并记录售出的位置
        # # 若售出位置位于末尾，则直接返回最大值
        # # 若售出位置位于中间，则下一次购入位置位于其后
        # # 当count==0时，则返回两次利润的相加
        # count = 2
        # for i in range(0, len(prices)):  # 外层
        #     if count == 0:  # 最多两次
        #         break
        #     maxProfit = 0  # 初始化最大利润
        #     for j in range(i + 1, len(prices)):  # 内层
        #         maxProfit = max((prices[j] - prices[i]), maxProfit)  # 在第i天买入在第j天抛出时的利润
        #     count -= 1
        #     if i == len(prices) - 1:  # 到达末尾
        #         break
        #
        # 与II不同的是，只有两次购买与售出的机会，所以不能以每天的利润相加进行计算
        # 一共具有两种获取利润的方式，一种是只一次交易便达到最大利润 ；第二种是完成两次交易达到最大利润
        # 因为求的还是最大利润，所以依然可以使用每天获得的利润进行计算
        # 所以还是使用动态规划的算法进行利润的计算
        # 能获取利润的由两种状态即完成一次交易和完成两次交易
        # 对于边界条件，初试利润都是0，，买入都是从第一天开始计算。

        profit1 = profit2 = 0  # 初始利润
        cost1 = cost2 = -prices[0]  # 买入的价格
        for i in range(1, len(prices)):  # 从第一个元素开始规划
            # 进行状态转移
            cost1 = max(cost1, -prices[i])  # 选择花费小的一天并进行状态转移,花费为负数
            profit1 = max(profit1, cost1 + prices[i])  # 计算利润
            cost2 = max(cost2, profit1 - prices[i])  # 以上一次的利润作为购入的本金即将状态1 转移到状态2中
            profit2 = max(cost2 + prices[i], profit2)
        print(profit1)
        print(profit2)
        resProfit = max(profit1, profit2)  # 去两个状态中最大的那个并返回
        print(resProfit)
        return profit2

if __name__ == '__main__':
    Test = Solution()
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    Test.maxProfit(prices)
