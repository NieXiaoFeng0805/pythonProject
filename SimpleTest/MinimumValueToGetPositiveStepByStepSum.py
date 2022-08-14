# @Time: 2022/8/9 14:02
# @Author: 丨枫
# @File MinimumValueToGetPositiveStepByStepSum.py
class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        # 暴力解法
        """
        for i in range(1, 10000):
            flag = True
            count_sum = i
            for j in nums:
                count_sum += j
                if count_sum < 1:
                    flag = False
                    break
            if flag:
                print(i)
                return i
        """

        # 优化:贪心
        accSum, accSumMin = 0, 0  # 记录累加和和累加过程中的最小值
        for i in nums:
            accSum += i  # 进行累加
            accSumMin = min(accSumMin, accSum)  # 记录最小和
        return -accSumMin + 1


if __name__ == '__main__':
    Test = Solution()
    nums = [-3, 2, -3, 4, 2]
    Test.minStartValue(nums)
