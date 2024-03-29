# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/16 10:47
# software: PyCharm
"""
文件说明：
1. 无序数组，需要找出最长的递增子序列
2. 简化版：无序数组，需要找出最长的递增子序列长度
"""


class Solution:
    def find_maxlen(self, nums, i):
        '''
        返回从数组第i个数字开始的最长子序列长度————没有优化的时间复杂度为（n*2^n）
        :param nums: 数组
        :param i: 当前位置
        :return: 当前位置开始的最长子序列长度
        '''

        if i == len(nums) - 1:  # 起始点最后一位，返回长度1
            return 1
        maxlen = 1
        for j in range(i + 1, len(nums)):

            # 比当前数大,能构成递增子序列
            if nums[j] > nums[i]:
                # self.find_maxlen(nums, j)  # 递归调用
                maxlen = max(maxlen, self.find_maxlen(nums, j) + 1)  # +1 是还要包含当前数
        return maxlen

    def optimize_find_maxlen(self, nums, i, memo):
        # 使用字典记录之前已经找过的子序列长度 —— 例如  [1,2,4]与 [4]，在[1,2,4]的时候就已经知道后续没有数了
        # 所以在i == 4 时直接返回 之前记录过的长度
        # 经过优化后的递归！！！

        # 记忆化搜索,若有之前的记录则直接返回
        if i in memo:
            return memo[i]
        if i == len(nums) - 1:
            return 1
        maxlen = 1
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                maxlen = max(maxlen, self.optimize_find_maxlen(nums, j, memo) + 1)
        memo[i] = maxlen  # 记录当前下标起始的最长子序列长度
        return maxlen

    # def lengthOfLIS(self, nums):
    #     '''
    #     主体函数————递归做法
    #     :param nums:
    #     :return:
    #     '''
    #     memo = {}
    #     # return max(self.find_maxlen(nums, i) for i in range(len(nums)))
    #     res = max(self.optimize_find_maxlen(nums, i, memo) for i in range(len(nums)))
    #     print(res)
    #     return res
    def lengthOfLIS(self, nums):
        '''
        主体函数———— 非递归
        :param nums:
        :return:
        '''
        n = len(nums)
        L = [1] * n  # 初始值，每个位置起始长度都为1
        for i in reversed(range(n)):  # 从后往前依次计算
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    L[i] = max(L[i], L[j] + 1)


        return max(L)


Solution().lengthOfLIS(nums=[1, 5, 2, 4, 3])
