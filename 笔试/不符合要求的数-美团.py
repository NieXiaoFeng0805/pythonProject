# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/16 16:02
# software: PyCharm
"""
文件说明：
美团某部门在拍年度纪念照时，一般要求员工按照 非递减 的高度顺序排列。请你返回至少有多少个员工没有站在正确位置数量。该人数指的是:能让所有员工以 非递减 高度排列的必要移动人数。
例如:有高度为 11,4.2.1,3 的6个学生共有3个学生没有站在正确的位置(高度为 4、3 和最后一个1的学生，没有站在正确的位置)
如遇到空输入的情况，需输出0
"""


class Solution:
    def create_num(self):
        return [int(x) for x in input().split(',')]

    def so(self):
        num_list = self.create_num()
        n = len(num_list)
        if n == 0:
            print(0)
        else:
            correct_list = sorted(num_list)
            res = 0
            for i in range(n):
                if correct_list[i] != num_list[i]:
                    res += 1
            print(res)


Solution().so()
