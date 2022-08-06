# @Time: 2022/8/4 12:29
# @Author: 丨枫
# @File MaxSumofaPairWithEqualSumofDigits.py
# 2342
from collections import defaultdict


class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return -1

        """       
        nums.sort(reverse=True)
        res = []
        theSum = -1
        for i in nums:
            count = 0  # 计算数位和
            temp = list(str(i))  # 先转字符串再转列表
            print(temp)
            for j in temp:  # 遍历列表将数位相加
                count += int(j)
            res.append(count)  # 添加到位数和列表，其索引一一对应
        rescopy = res.copy()
        res.sort(reverse=True)
        for v in res:
            if res.count(v) >= 2:
                theSum += nums[rescopy.index(v)]
                rescopy.remove(v)
                theSum += nums[rescopy.index(v) + 1]
                break
        print(theSum)
        return theSum
        """
        res = -1  # 默认返回值
        nums_dict = defaultdict(int)  # 创建字典
        for i in nums:
            count = 0  # 计算数位和
            temp = list(str(i))  # 先转字符串再转列表
            # print(temp)
            for j in temp:  # 遍历列表将数位相加
                count += int(j)
            if count in nums_dict:  # 若字典中有这个键
                res = max(res, nums_dict[count] + i)  # 维护最大值
            nums_dict[count] = max(nums_dict[count], i)  # 添加新元素到字典中，若是小于当前值的则不要
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    nums = [368, 369, 307, 304, 384, 138, 90, 279, 35, 396, 114, 328, 251, 364, 300, 191, 438, 467, 183]
    Test.maximumSum(nums)
