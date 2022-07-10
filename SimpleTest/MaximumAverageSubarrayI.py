# @Time: 2022/7/5 19:37
# @Author: 丨枫
# @File MaximumAverageSubarrayI.py
from cmath import inf


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # 已超时
        """
        thesum = float('-inf')
        i = 0
        while (i + k - 1) < len(nums):
            # 求窗口最大值
            thesum = max(sum(nums[i:(i + k)]), thesum)
            i += 1

        print(thesum/k)
        return thesum/k"""

        # 优化
        theSum = 0
        largest = float(-inf)
        for index, val in enumerate(nums):
            theSum += val
            if index >= k:  # 到窗口右边界，删除窗口左边界的值
                theSum -= nums[index - k]
            if index >= k - 1:  # 临界，计算当前窗口和
                largest = max(largest, theSum)
        return largest / k


if __name__ == '__main__':
    Test = Solution()
    nums, k = [-1], 1
    Test.findMaxAverage(nums, k)
