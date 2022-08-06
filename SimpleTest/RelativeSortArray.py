# @Time: 2022/8/1 13:01
# @Author: 丨枫
# @File RelativeSortArray.py
class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        notInArray, hasInArray = [], []  # 存放不在arr2中的和在arr2中的数
        for i in arr2:  # 找存在于arr2中的数
            n = arr1.count(i)
            hasInArray += [i for _ in range(n)]

        for i in arr1:  # 找不存在arr2中的数
            if i not in arr2:
                notInArray.append(i)
        notInArray.sort()  # 对不存在arr2中的数进行排序
        res = hasInArray + notInArray
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    arr1, arr2 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]
    Test.relativeSortArray(arr1, arr2)
