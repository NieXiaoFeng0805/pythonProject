# @Time: 2022/9/19 15:39
# @Author: 丨枫
# @File Sort Array by Increasing Frequency.py
from collections import Counter


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        num_dict = Counter(nums)
        """
        temp = []
        print(num_dict)
        while num_dict:
            i_key, i_value = 0, 0
            for k, v in num_dict.items():
                if v > i_value:
                    i_key = k
                    i_value = v
            temp.append([i_key] * i_value)
            num_dict.pop(i_key)
        res = sorted(temp, key=len)
        print(res)
        for j in range(len(res)):
            for i in range(1, len(res)):
                if res[i - 1][0] < res[i][0] and len(res[i - 1]) == len(res[i]):
                    a = res[i - 1]
                    res[i - 1] = res[i]
                    res[i] = a
        print(sum(res, []))
        return sum(res, [])"""

        # 优化
        nums_list = []
        res = []
        for k, v in num_dict.items():
            nums_list.append([k, v])
        print(nums_list)
        nums_list = sorted(nums_list, key=lambda x: (x[1], -x[0]))
        print(nums_list)
        for i in nums_list:
            res += [i[0]] * i[1]
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    Test.frequencySort(nums=[-8, 7, -1, 3, 5, 7, -8, -8, 0])
