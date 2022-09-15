# @Time: 2022/9/8 15:10
# @Author: 丨枫
# @File Max Consecutive Ones.py
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        maxCount = 0
        for i in nums:
            if i == 1:
                count += 1
                temp = count
            else:
                count = 0
                continue
            maxCount = max(temp, maxCount)
        print(maxCount)
        return maxCount


if __name__ == '__main__':
    Test = Solution()
    Test.findMaxConsecutiveOnes(nums=[1, 1, 0, 1, 1, 1])
