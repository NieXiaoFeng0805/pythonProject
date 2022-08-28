# @Time: 2022/8/26 10:51
# @Author: 丨枫
# @File Maximum Product of Two Elements in an Array.py
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # 遍历两次，找两次最大值
        """
        n = 2
        sum = 1
        for i in range(n):
            max_num = max(nums)
            max_index = nums.index(max_num)
            sum *= max_num - 1
            nums[max_index] = -1
        print(sum)
        return sum"""

        # 排序
        """nums.sort()
        return (nums[-1]-1) * (nums[-2]-1)"""
        # 一次遍历维护最大值次大值
        first_num, second_num = 0, 0
        for i in nums:
            if i > first_num:
                first_num, second_num = i, first_num
            elif i > second_num:
                second_num = i
        return (first_num - 1) * (second_num - 1)

        # 维护前k大值模板

        """
    # 前k小去掉这里面的所有负号
        def find_k_max(arr: List[int], k: int) -> List[int]:
            ans = []
            for num in arr:
                idx = bisect_left(ans, -num)
                if idx < k:
                    if idx == len(ans):
                        ans.append(-num)
                    else:
                        ans = ans[:idx] + [-num] + ans[idx:]
                        if len(ans) > k:
                            ans.pop()
            return [-num for num in ans]
        
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (ans[-1] - 1) * (ans[-2] - 1) if (ans := find_k_max(nums, 2)) else 0"""


if __name__ == '__main__':
    Test = Solution()
    Test.maxProduct(nums=[1, 5, 4, 5])
