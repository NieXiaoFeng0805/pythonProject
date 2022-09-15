# @Time: 2022/9/6 14:53
# @Author: 丨枫
# @File House to steal.py
class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[size - 1]


if __name__ == '__main__':
    Test = Solution()
    Test.rob(nums=[2, 7, 9, 3, 1])
