# @Time: 2022/8/13 11:16
# @Author: 丨枫
# @File Check if There is a Valid Partition For The Array.py
class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        # 动态划分
        n = len(nums)
        f = [True] + [False] * n
        for i, x in enumerate(nums):
            if i > 0 and f[i - 1] and x == nums[i - 1] or \
                    i > 1 and f[i - 2] and (x == nums[i - 1] == nums[i - 2] or
                                            x == nums[i - 1] + 1 == nums[i - 2] + 2):
                f[i + 1] = True
        return f[n]


if __name__ == '__main__':
    Test = Solution()
    Test.validPartition(nums=[4, 4, 4, 5, 6])
