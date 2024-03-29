# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/9 11:24
# software: PyCharm
"""
文件说明：
1. 正整数数组，其中有未知元素（用0表示）
2. 若未知元素在区间[l,r]范围内随机取值，则数组所有元素之和的最小值和最大值分别是多少

"""


class Solution:
    def find_min_max(self):
        count, other_sum, q_list = self.create_num()
        # 最小值取左边界，最大值取右边界
        for i in q_list:
            l, r = i[0], i[1]
            min_s = other_sum + l * count
            max_s = other_sum + r * count
            print(min_s, max_s)

    def create_num(self):
        nq = input().split()  # 数组大小\询问次数
        n, q = int(nq[0]), int(nq[1])
        num_list = input().split()
        count = 0
        other_sum = 0
        for i in num_list:
            if int(i) == 0:
                count += 1
            else:
                other_sum += int(i)
        q_list = []
        for j in range(q):
            the_q = input().split()
            q_list.append([int(the_q[0]), int(the_q[1])])
        return count, other_sum, q_list


if __name__ == '__main__':
    Solution().find_min_max()
