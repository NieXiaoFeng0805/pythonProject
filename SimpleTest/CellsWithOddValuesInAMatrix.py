# @Time: 2022/7/15 11:27
# @Author: 丨枫
# @File CellsWithOddValuesInAMatrix.py


class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        matrix = [[0] * n for _ in range(m)]  # 创建二维零矩阵
        res = 0  # 返回值
        for point in indices:  # 每个指令中的行和列
            ri = point[0]
            ci = point[1]

            for i in range(n):  # 每列元素+1
                matrix[ri][i] += 1
            for i in range(m):  # 每行元素+1
                matrix[i][ci] += 1

        for i in range(m):  # 遍历操作后的矩阵，若是奇数则结果+1
            for j in range(n):
                if matrix[i][j] & 1 == 1:
                    res += 1

        return res


if __name__ == '__main__':
    Test = Solution()
    m, n, indices = 2, 3, [[0, 1], [1, 1]]
    Test.oddCells(m, n, indices)
