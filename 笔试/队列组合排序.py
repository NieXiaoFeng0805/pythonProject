# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/8 22:21
# software: PyCharm
"""
文件说明：
要求：
交叉前：队列[男1，男2，男3，男4…男n，女1，女2，女3，女4…女n]
交叉后：队列[男1，女1，男2，女2，男3，女3，男4，女4…男n，女n]

输入第一行一个整数 n 表示有 n 个男生和 n 个女生
第 2 到第 n+1 行每一行有一个数字表示每个男生的编号
第 n+2 到第 2*n+1 行每一行有一个数字表示每个女生的编号

输出 2*n 行，每行一个名字表示交叉排列后队列中依次每个学生的编号
"""


class Solution:
    def insert_queue(self):
        # 创建两个列表存放
        n, num_list = self.createList()
        for i in range(n):
            print(num_list[i])
            print(num_list[i + n])

    def createList(self):
        n = int(input())
        num_list = [int(input()) for _ in range(2 * n)]
        return n, num_list


if __name__ == '__main__':
    Solution().insert_queue()
