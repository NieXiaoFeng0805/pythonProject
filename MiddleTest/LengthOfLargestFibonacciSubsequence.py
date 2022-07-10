# @Time: 2022/7/9 17:42
# @Author: 丨枫
# @File LengthOfLargestFibonacciSubsequence.py
from collections import defaultdict


class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # 垃圾
        """
        # 设置两个指针，标识i-2和i-1个数
        left, right = 0, 1
        flag = True  # 标识是否存在子序列
        res = []  # 子序列中的数目
        count_fib = 2  # 计数
        while left < len(arr) - 1:
            while right < len(arr):
                if arr[left] + arr[right] in arr:  # 能组成子序列
                    flag = False
                    count_fib += 1
                    left = right
                    right = arr.index(arr[left] + arr[right])
                else:
                    right+=1
            left += 1
            right = left + 1
        if flag:
            return 0
        print(res)
        return len(res)"""

        arr_length = len(arr)
        numsToindexDict = {num: i for i, num in enumerate(arr)}
        flag = True  # 标识是否能组成子序列
        res = 2
        # 状态转移
        dp = defaultdict(lambda: defaultdict(lambda: 2))  # defaultdict能当键不在字典中时返回默认值而不是错误
        print(list(dp))
        for i in range(arr_length - 1):
            for j in range(i + 1, arr_length):
                temp = arr[i] + arr[j]
                if temp in numsToindexDict:  # 能组成子序列
                    flag = False
                    dp[j][numsToindexDict[temp]] = dp[i][j] + 1
                    res = max(res, dp[j][numsToindexDict[temp]])
        if flag:
            return 0
        print(res)
        return res

if __name__ == '__main__':
    Test = Solution()
    arr = [1, 3, 7, 11, 12, 14, 18]
    Test.lenLongestFibSubseq(arr)
