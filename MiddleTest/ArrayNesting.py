# @Time: 2022/7/22 11:42
# @Author: 丨枫
# @File ArrayNesting.py
from pyparsing import nums


class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        # 超时
        """
        count = []  # 存储最长嵌套子序列长度
        for i in range(len(nums)):
            if nums[i] == len(nums) + 1:
                continue
            num_list = []  # 存储不重复数字
            j = i
            while True:
                temp = nums[j]
                num_list.append(j)
                if temp in num_list:
                    break
                j = temp
            count.append(len(num_list))
            # 将出现过的数改为len+1，以免重复计算
            for k in num_list:
                nums[k] = len(nums) + 1
        print(count)
        return max(count)"""

        # 优化
        res = 0  # 返回最长长度
        for i in range(len(nums)):
            if nums[i] == len(nums) + 1:  # 避免重复计算
                continue
            next_index = nums[i]  # 下一个元素所对应的索引
            depth = 1  # 长度最小为1
            while next_index != i:  # 当下一个元素的值等于当前元素的索引时跳出循环
                temp = nums[next_index]  # 临时存储下一个元素对应的索引
                nums[next_index] = len(nums) + 1  # 将用过的数改成无法再次使用
                depth += 1  # 长度+1
                next_index = temp  # 赋值
            res = max(res, depth)
        return res


if __name__ == '__main__':
    Test = Solution()
    nums = [5, 4, 0, 3, 1, 6, 2]
    Test.arrayNesting(nums)
