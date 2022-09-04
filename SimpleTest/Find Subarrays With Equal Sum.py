# @Time: 2022/9/4 14:48
# @Author: 丨枫
# @File Find Subarrays With Equal Sum.py
class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False
        n = len(nums)
        if nums.count(0) == n:
            return True
        # 若存在两个子数组的和相等，则原数组必然不可能是升序排列的
        nums_sort = sorted(nums)
        if nums_sort == nums:
            return False
        # 将原数组中的两个数两两相加成为新数组，有重复元素说明存在这样的子数组
        l, r = 0, 1

        sum_list = []
        while r < n:
            sum_list.append(nums[l] + nums[r])
            l += 1
            r += 1
        return len(set(sum_list)) != len(sum_list)


if __name__ == '__main__':
    Test = Solution()
    Test.findSubarrays(nums=[1, 2, 3, 4, 3, 5])
