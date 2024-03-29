# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/17 9:54
# software: PyCharm
"""
文件说明：

"""
import math


class Solution:
    def create_num(self):
        n, m = [int(x) for x in input().split()]
        num_list = []
        for i in range(m):
            if not num_list:
                num_list.append(n)
            else:
                num_list.append(math.sqrt(n))
                n = math.sqrt(n)
        return n, m, num_list

    def solution(self):
        n, m, numlist = self.create_num()
        print('%.2f' % sum(numlist))


Solution().solution()
