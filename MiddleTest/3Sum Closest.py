# @Time: 2022/8/26 11:13
# @Author: 丨枫
# @File 3Sum Closest.py
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        minClose = 10 ** 7
        def minSum(cur):
            nonlocal minClose
            if abs(cur - target) < abs(minClose - target):
                minClose = cur
        for val in range(n):
            if val > 0 and nums[val] == nums[val - 1]:
                continue
            L, R = val + 1, n - 1  # 设置双指针从两端遍历
            while L < R:
                nums_sum = nums[val] + nums[L] + nums[R]  # 记录和
                if nums_sum == target:  # 刚好相等，因为只有一个解，直接返回
                    return target
                minSum(nums_sum)
                if nums_sum > target:  # 相加大于target，右边大了，右指针往左移动
                    R = R - 1
                else:  # 相加小于target，左指针往右移动
                    L = L + 1
        print(minClose)
        return minClose


if __name__ == '__main__':
    Test = Solution()
    Test.threeSumClosest(nums=[1, 1, 1, 0], target=-100)
