# @Time: 2022/6/17 13:53
# @Author: 丨枫
# @File DuplicateZeros.py
from colorcet.plotting import arr


class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # 原地修改，记录添加0的次数，等循环到原列表末尾时在弹出添加个数的值
        arrLens = len(arr)
        count = 0
        i = 0
        if 0 not in arr:  # 没有0的情况
            return arr

        while i <= arrLens:
            if arr[i] == 0:
                arr.insert(i, 0)
                count += 1
                i += 2
                continue
            i += 1
        print(arr)
        for j in range(len(arr) - 1, - 1, -1):
            arr.pop(j)
            count -= 1
            if count == 0:
                break
        print(arr)
        return arr


if __name__ == '__main__':
    Test = Solution()
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    Test.duplicateZeros(arr)
