# @Time: 2022/8/9 14:57
# @Author: 丨枫
# @File NumberOfArithmeticTriplets.py
from pyparsing import nums


class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        count = 0  # 计算三元组的个数
        for i in nums:
            temp = i + diff
            if temp > max(nums) or temp + diff > max(nums):  # 无需再往下遍历了
                break
            if temp in nums and temp + diff in nums:
                count += 1
                continue
        print(count)
        return count


if __name__ == '__main__':
    Test = Solution()
    Test.arithmeticTriplets(nums=[0, 1, 4, 6, 7, 10], diff=3)
