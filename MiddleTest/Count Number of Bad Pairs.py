# @Time: 2022/8/29 13:43
# @Author: 丨枫
# @File Count Number of Bad Pairs.py
class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        # 暴力解法 超时
        """
        nums_len = len(nums)
        count = 0  # 记录坏数对
        if nums_len == 1:
            return 0
        if nums_len == 2:
            return 1 if (nums[1] - nums[0] == 1) else 0
        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                if nums[j] - nums[i] < 0 or nums[j] - nums[i] != j - i:
                    count += 1
                else:
                    continue
        print(count)
        return count"""

        # 转变成 nums[j] - j != nums[i]-i
        nums_len = len(nums)
        if nums_len == 1:
            return 0
        sum_count = (nums_len * (nums_len - 1)) // 2  # 总可能数
        subDict = {}  # 记录差值
        for index, val in enumerate(nums):
            temp = val - index
            if temp in subDict:
                sum_count -= subDict[temp]
                subDict[temp] += 1
            else:
                subDict[temp] = 1

        print(sum_count)
        return sum_count


if __name__ == '__main__':
    Test = Solution()
    # Test.countBadPairs(
    #     nums=[56, 30, 2, 73, 28, 81, 75, 75, 18, 63, 54, 10, 69, 85, 33, 89, 12, 78, 57, 60, 54, 65, 74, 63, 53, 77])
    Test.countBadPairs(
        nums=[1, 2, 3, 4, 5])
