# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/19 11:53
# software: PyCharm
"""
文件说明：
对一个 n*n 的矩阵， 矩阵由0,1组成
当且仅当 i*i 区域内的0,1数量相等时————称为完美矩阵
要求： 输出 1 <= i <= n 的所有完美矩阵
"""


class Solutioin:
    def create_matrix(self):
        n = int(input())
        matrix_list = []
        for _ in range(n):
            num_str = list(map(int, input()))
            matrix_list.append(num_str)
        return n, matrix_list

    def solution(self):
        n, matrix = self.create_matrix()

        # 边长
        for i in range(1, n + 1):
            # 起始位置数组
            if i == 1:
                print(0)
                continue
            res = 0
            start_list = [j for j in range(n - i + 1)]
            for row in start_list:
                start_row = row
                for col in start_list:
                    start_col = col
                    flag = self.judge_single_per(matrix, start_row, start_col, i)
                    if flag:
                        res += 1
            print(res)

    def judge_single_per(self, matrix, start_row, start_col, i):
        '''
        确定单个矩阵是否是完美矩阵
        :param matrix:
        :param n:
        :param i:
        :return:
        '''
        cnt_0, cnt_1 = 0, 0  # 记录0,1的个数
        for r in range(start_row, start_row + i):
            for c in range(start_col, start_col + i):
                if matrix[r][c] == 0:
                    cnt_0 += 1
                else:
                    cnt_1 += 1
        if cnt_0 == cnt_1:  # 完美矩阵
            return True
        else:
            return False


Solutioin().solution()
