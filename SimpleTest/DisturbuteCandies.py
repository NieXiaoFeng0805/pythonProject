# @Time: 2022/8/1 12:04
# @Author: 丨枫
# @File DisturbuteCandies.py
class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        """
        eat_total = len(candyType) / 2  # 能吃的的糖个数
        eat_kinds = len(set(candyType))  # 糖的种类

        print(eat_kinds)
        if eat_total > eat_kinds:  # 能吃的糖的个数大于糖的种类,可以吃到全部的糖种类
            return eat_kinds
        else:  # 糖种类大于能吃的糖的个数，则只能吃到较小的糖种类
            return int(eat_total)"""

        # 优化，只返回能吃到的糖和糖种类中的较小数
        eat_total = len(candyType) / 2  # 能吃的的糖个数
        eat_kinds = len(set(candyType))  # 糖的种类
        return eat_kinds if eat_total > eat_kinds else int(eat_total)

if __name__ == '__main__':
    Test = Solution()
    candyType = [1, 1, 2, 2, 3, 3]
    Test.distributeCandies(candyType)
