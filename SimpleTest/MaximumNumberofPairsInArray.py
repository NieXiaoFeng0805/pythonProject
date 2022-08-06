# @Time: 2022/8/4 12:06
# @Author: 丨枫
# @File MaximumNumberofPairsInArray.py
class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return [0, 1]
        nums_dict = {key: nums.count(key) for value, key in enumerate(nums)}

        # print(nums_dict)
        count = 0  # 计算数对
        count_odd = 0  # 计算能剩下的数
        for i in nums_dict:
            if nums_dict[i] % 2 == 0:  # 偶数才有数对
                count += nums_dict[i] // 2
            elif nums_dict[i] > 2 and nums_dict[i] % 2 != 0:  # 奇数但能组成对子
                count += nums_dict[i] // 2
                count_odd += 1
            else:  # 不能组成对子
                count_odd += 1

        print([count, count_odd])
        return [count, count_odd]


if __name__ == '__main__':
    Test = Solution()
    nums = [1, 2, 3, 4, 5]
    Test.numberOfPairs(nums)
