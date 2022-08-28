# @Time: 2022/8/24 12:39
# @Author: 丨枫
# @File Largest Local Values in a Matrix.py
"""
最大池化
"""


class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)  # 矩阵维度
        size = 3  # 卷积核大小
        res = [[0] * (n - size + 1) for _ in range(n - size + 1)]  # 返回矩阵

        # print(res)

        def findMaxValue(grid, i, j, size):  # 找最大值
            maxVal = grid[i][j]
            for v in range(i, i + size):
                for k in range(j, j + size):
                    if grid[v][k] >= maxVal:
                        maxVal = grid[v][k]
            return maxVal

        # 遍历结果矩阵
        for i in range(n - size + 1):
            for j in range(n - size + 1):
                res[i][j] = findMaxValue(grid, i, j, size)
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    Test.largestLocal(grid=[[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]])
