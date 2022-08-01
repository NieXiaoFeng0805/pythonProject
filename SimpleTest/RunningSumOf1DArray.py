# @Time: 2022/7/26 16:22
# @Author: 丨枫
# @File RunningSumOf1DArray.py
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        """
        res = [nums[0]]
        temp = 0
        for i in nums:
            temp += i
            res.append(temp)
        res.pop(0)
        print(res)
        return res"""

        # 优化
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        print(nums)
        return nums


if __name__ == '__main__':
    Test = Solution()
    nums = [3, 1, 2, 10, 1]
    Test.runningSum(nums)
