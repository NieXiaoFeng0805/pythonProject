# author: Feng
# contact: 1245272985@qq.com
# datetime:2022/10/16 11:42
# software: PyCharm
"""
文件说明：

"""


class Solution:
    def countSubarrays(self, nums: list, minK: int, maxK: int) -> int:
        min_k, max_k = [], []
        n = len(nums)
        for i in range(n):
            if nums[i] == minK:
                min_k.append(i)
            if nums[i] == maxK:
                max_k.append(i)
        print(min_k, max_k)
        count = 0
        for i in min_k:
            for j in max_k:
                temp = nums[i:j + 1]
                if max(temp) == maxK:
                    count += 1
                print(temp)


if __name__ == '__main__':
    Test = Solution()
    Test.countSubarrays(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5)
