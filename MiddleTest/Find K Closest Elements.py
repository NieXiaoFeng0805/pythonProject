# @Time: 2022/8/25 11:52
# @Author: 丨枫
# @File Find K Closest Elements.py
from bisect import bisect_left


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        if x <= arr[0]:  # 小于最小的数
            return arr[0:k]
        if x >= arr[-1]:  # 大于最大的数
            return arr[-k:]
        # 一般做法
        """
        # 在中间，则计算出数组中的每个数与x的差值的绝对值
        sub_arr = [abs(i - x) for i in arr]
        print(sub_arr)
        # 找到最小差值
        min_index = sub_arr.index(min(sub_arr))
        res = []  # 返回列表
        # 从左边找起
        boder = min_index - k
        if boder < 0:
            res.extend(arr[0:k])
            print(res)
            # 从右边找看是否能替代
            for j in arr[k:]:
                if j - x < abs(res[0] - x):  # 找到更小的
                    res.pop(0)
                    res.append(j)
        else:
            res.extend(arr[min_index - k + 1:min_index + 1])
            print(res)
            # 从右边找看是否能替代
            for j in arr[min_index + 1:2 * min_index]:
                if j - x < abs(res[0] - x):  # 找到更小的
                    res.pop(0)
                    res.append(j)
        print(res)
        return res"""

        # 二分法
        r = bisect_left(arr, x)
        l = r - 1
        while k:
            if l < 0:
                r += 1
            elif r == len(arr):
                l -= 1
            else:
                if x - arr[l] <= arr[r] - x:
                    l -= 1
                else:
                    r += 1
            k -= 1
        return arr[l + 1:r]


if __name__ == '__main__':
    Test = Solution()
    # Test.findClosestElements(arr=[0, 1, 2, 2, 2, 3, 6, 8, 8, 9], k=5, x=9)
    Test.findClosestElements(arr=[1, 3, 5, 7, 9, 10, 12, 14, 15], k=3, x=9)
