# @Time: 2022/7/7 12:54
# @Author: 丨枫
# @File FrequencyOfTheMostFrequentElement.py
from pyparsing import nums


class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 先排序
        nums.sort()
        print(nums)

        left, right = 0, 0
        ele_sum = 0  # 元素之和
        res = 0
        while right < len(nums):
            ele_sum += nums[right]  # 将元素相加
            while ele_sum + k < nums[right] * (right - left + 1):  # 当当前元素和+k值小于右边界的值*窗口长度时，左边界移动
                ele_sum -= nums[left]
                left += 1
            res = max(res, right - left + 1)  # 更新最大长度
            right += 1
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    nums, k = [3, 9, 6], 5
    Test.maxFrequency(nums, k)
