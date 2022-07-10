# @Time: 2022/7/4 11:13
# @Author: 丨枫
# @File MinimumAbsoluteDifference.py
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        """
        # 先排序
        newarr = sorted(arr)
        print(newarr)

        res = []  # 返回列表
        print(res)
        # 设置两个游标进行最小差值的计算
        pre, last = 0, 1
        # 找到最小差值
        min_sub = newarr[1] - newarr[0]
        while pre < len(newarr) - 1:
            min_sub = min(newarr[last] - newarr[pre], min_sub)
            last += 1
            pre += 1
        print(min_sub)
        # 再次遍历，差值为min_sub的添加到返回列表中
        for i in range(1, len(newarr)):
            if (newarr[i] - newarr[i - 1]) == min_sub:
                res.append([newarr[i - 1], newarr[i]])
        print(res)
        return res"""

        # 优化#
        # 先排序
        newarr = sorted(arr)
        print(newarr)
        res = []
        min_start = newarr[1] - newarr[0]
        # 遍历，找到当前最小的差值，添加元素对，若找到新的最小差值则清空列表并重新添加
        for i in range(1, len(newarr)):
            min_sub = newarr[i] - newarr[i - 1]
            if min_sub == min_start:  # 当前最小差值
                res.append([newarr[i - 1], newarr[i]])
            if min_sub < min_start:  # 找到更小的差值
                min_start = min_sub  # 更新差值
                res.clear()  # 清空列表
                res.append([newarr[i - 1], newarr[i]])  # 重新添加
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    arr = [40, 11, 26, 27, -20]
    Test.minimumAbsDifference(arr)
