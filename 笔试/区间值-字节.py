# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/15 9:40
# software: PyCharm
"""
文件说明：

"""

# 给定数组序列， 满足 区间中最小数*区间所有数的和； 取最大值
#
# class Solution:
#     def create_list(self):
#         n = int(input())
#         str_list = input().split()
#         num_list = [int(i) for i in str_list]
#         return n, num_list
#
#     def solution(self):
#         n, num_list = self.create_list()
#         num_list.sort()
#         # 最大值
#         max_num = 0
#         # 从后往前遍历
#         num_sum = 0
#         for i in range(n - 1, -1, -1):
#             num_sum += num_list[i]
#             max_num = max(max_num, num_sum * num_list[i])
#         print(max_num)
#
#
# # num_list[-1] * num_list[-1]
# Solution().solution()

# 答案， 不能排序！！！！
# n = int(input())
# arr = [int(x) for x in input().split()]
n = 8
arr = [3, 6, 2, 1, 4, 5, 7, 9]
stack = []
arr.append(0)
result = 0
i = 0
presum = []
tempsum = 0
while i < len(arr):
    if not stack or arr[i] >= stack[-1]:
        presum.append(tempsum)
        tempsum = 0
        stack.append(arr[i])
        i += 1
    else:
        temp = stack.pop(-1)
        tempsum += (temp + presum.pop())
        result = max(tempsum * temp, result)
print(result)
