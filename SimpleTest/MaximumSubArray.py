# @Time: 2022/6/6 13:47
# @Author: 丨枫
# @File MaximumSubArray.py
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        1、若当前指针所指的元素之前的和当前元素则将当前元素作为当前和
        2、否则将当前和与最大和比较
        """
        # 若列表元素都是负数，则返回最大的那个
        Flag = True
        for i in nums:
            if i > 0:
                Flag = False
                break
        if Flag:
            return max(nums)
        # 若列表元素只有1个，则返回
        if len(nums) == 1:
            return nums[0]

        cur_sum = nums[0]  # 当前和
        max_sum = nums[0]  # 最大和
        for i in range(1, len(nums)):
            cur_sum = cur_sum + nums[i]  # 当前值与之前值相加
            if nums[i] > cur_sum:  # 若当前值更大
                cur_sum = nums[i]  # 则替换当前和为当前值
            max_sum = max(cur_sum, max_sum)  # 否则将当前和与最大和作比较，取较大值
        print(max_sum)
        return max_sum

        # 贪心实现
        """cur_sum = max_sum =nums[0] #赋初值
        for i in range(1,len(nums)):
            cur_sum = max(nums[i],cur_sum+nums[i])
            max_sum = max(cur_sum,max_sum)
        return max_sum
"""

        # 动态规划实现
        """n = len(nums)
        for i in range(1, n):
            if nums[i - 1] > 0:  # 若前一个数大于0
                nums[i] += nums[i - 1]  # 当前值为当前值与前值相加
        print(max(nums))
        return max(nums)"""


if __name__ == '__main__':
    Test = Solution()
    nums = [5, 4, -1, 7, 8]
    Test.maxSubArray(nums)
