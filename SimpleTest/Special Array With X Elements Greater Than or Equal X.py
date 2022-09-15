# @Time: 2022/9/12 17:06
# @Author: 丨枫
# @File Special Array With X Elements Greater Than or Equal X.py
from collections import Counter


class Solution:
    def specialArray(self, nums: list[int]) -> int:
        res = -1
        n = len(nums)
        nums.sort()
        if nums[0] >= n: # 最小值大于等于其长度
            print(n)
            return n
        for x in range(n):
            for j in range(n):
                if nums[j] >= x:
                    if n - j == x:
                        res = x
                        print(res)
                    break
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    Test.specialArray(nums=[3, 5])
