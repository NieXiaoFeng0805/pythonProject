# @Time: 2022/9/3 10:54
# @Author: 丨枫
# @File Maximum Length of Pair Chain.py
from itertools import chain
from math import inf


class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        # resList = list(set(chain.from_iterable(pairs)))  # 合并二维数组并去重，因为原顺序就是升序，不用排序
        res = []
        pairs.sort()
        for i in pairs:
            if not res:
                res.append(i)
            elif i[1] < res[-1][1]:  # 当前值的较大数小于结果数组中最后一个组的较大数,说明该组作为起点会更好
                res.pop()
                res.append(i)
            elif i[0] > res[-1][1]:  # 当前值的较小数大于结果数组中最后一个组的第二个数，说明可以连接起来
                res.append(i)
        return len(res)


if __name__ == '__main__':
    Test = Solution()
    Test.findLongestChain(pairs=[[8, 9], [-10, -8], [-5, 0], [6, 10], [-6, -4], [1, 7], [9, 10], [-4, 7]])
