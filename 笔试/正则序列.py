# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/8 18:21
# software: PyCharm
"""
文件说明：
我们称一个长度为n的序列为正则序列，当且仅当该序列是一个由1~n组成的排列，即该序列由n个正整数组成，取值在[1,n]范围，且不存在重复的数，同时正则序列不要求排序

"""


class Solution:
    def min_set(self):
        n = int(input())
        num_list = list(map(int, input().split()))

        target_num_list = [i for i in range(1, n + 1)]  # 目标正则序列
        num_list.sort()  # 对原数组进行排序
        res = 0
        for i in range(n):
            res += abs(num_list[i] - target_num_list[i])  # 取对应位置数的绝对值，作为其每个位置上最小操作数
        print(res)


if __name__ == '__main__':
    Solution().min_set()
