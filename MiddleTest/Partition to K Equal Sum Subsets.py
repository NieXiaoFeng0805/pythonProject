# @Time: 2022/9/20 11:13
# @Author: 丨枫
# @File Partition to K Equal Sum Subsets.py
class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        def dfs(i):
            if i == len(nums):
                return True
            for j in range(k):
                if j and cur[j] == cur[j - 1]:
                    continue
                cur[j] += nums[i]
                if cur[j] <= s and dfs(i + 1):
                    return True
                cur[j] -= nums[i]
            return False

        s, mod = divmod(sum(nums), k)
        if mod:
            return False
        cur = [0] * k
        nums.sort(reverse=True)
        return dfs(0)


if __name__ == '__main__':
    Test = Solution()
    Test.canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=4)
