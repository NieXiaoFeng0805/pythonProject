# @Time: 2022/5/6 18:05
# @Author: 丨枫
# @File SearchInsertPosition.py
class Solution(object):
    def searchInsert(self, nums, target):
        for i, j in enumerate(nums):
            if j == target:
                return i
        # 不在列表内
        for i in range(len(nums) - 1, -1, -1):
            if nums[0] > target:
                return 1
            if target > nums[i]:
                return i + 1
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


if __name__ == '__main__':
    Test = Solution()
    nums = [1, 3, 5, 6]
    target = 2
    Test.searchInsert(nums, target)
