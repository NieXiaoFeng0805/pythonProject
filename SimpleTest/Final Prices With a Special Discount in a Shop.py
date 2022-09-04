# @Time: 2022/9/2 11:09
# @Author: 丨枫
# @File Final Prices With a Special Discount in a Shop.py
class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        n = len(prices)
        res = []
        for i in range(n):
            flag = True  # 判断是否有折扣
            for j in range(i + 1, n):
                if prices[j] > prices[i]:  # 没有折扣
                    continue
                else:  # 有折扣
                    flag = False
                    res.append(prices[i] - prices[j])
                    break
            if flag:
                res.append(prices[i])
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    Test.finalPrices(prices=[8, 4, 6, 2, 3])
