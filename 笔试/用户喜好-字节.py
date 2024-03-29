# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/15 19:50
# software: PyCharm
"""
文件说明：

"""


class Solution:
    def create_num(self):
        n = int(input())  # 用户数
        target = [int(x) for x in input().split()]
        sum_q = int(input())
        q_list = []
        for i in range(sum_q):
            q_list.append([int(x) for x in input().split()])
        return n, target, q_list

    def so(self):
        n, target, q_list = self.create_num()
        for q in q_list:
            l, r, k = q[0], q[1], q[2]
            cnt = 0
            for i in target[l - 1:r]:
                if i == k:
                    cnt += 1
            print(cnt)


Solution().so()
