# @Time: 2022/8/4 10:54
# @Author: 丨枫
# @File MinimumSubsequenceInNon-increasingOrder.py
class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        # print(nums[0:2],nums[2:])
        i = 0
        while True:
            if sum(nums[0:i]) > sum(nums[i:]):  # 找到严格大于的数了
                break
            i += 1
        print(nums[0:i])
        return nums[0:i]


if __name__ == '__main__':
    Test = Solution()
    nums = [4, 4, 7, 6, 7]
    Test.minSubsequence(nums)
