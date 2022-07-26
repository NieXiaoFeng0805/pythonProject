# @Time: 2022/7/21 15:20
# @Author: 丨枫
# @File Shift2DGrid.py
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        m = len(grid)  # 行
        n = len(grid[0])  # 列
        # print(m, n)

        def moveElement(grid, m, n):  # 移动元素
            newarr = [0] * m
            for i in range(len(newarr)):
                newarr[i] = [0] * n
            # print(newarr)
            newarr[0][0] = grid[m - 1][n - 1]
            for i in range(m):
                for j in range(1, n):
                    newarr[i][j] = grid[i][j - 1]
            for a in range(1, m):
                newarr[a][0] = grid[a - 1][n - 1]
            return newarr

        newarr = moveElement(grid, m, n)
        for i in range(k - 1):
            newarr = moveElement(newarr, m, n)
        print(newarr)
        return newarr"""

        # 优化
        m, n = len(grid), len(grid[0])  # 获得行、列
        k %= m * n  # 防止越界
        ans = [[0] * n for _ in range(m)]  # 初始化返回列表
        for i in range(m):
            for j in range(n):
                # divmod 把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
                x, y = divmod(i * n + j + k, n)
                # 更新返回数组
                ans[x % m][y] = grid[i][j]
        return ans


if __name__ == '__main__':
    Test = Solution()
    grid = [[1], [2], [3], [4], [7], [6], [5]]
    k = 4
    Test.shiftGrid(grid, k)
