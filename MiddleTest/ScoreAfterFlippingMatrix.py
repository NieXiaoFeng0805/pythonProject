# @Time: 2022/6/2 10:03
# @Author: 丨枫
# @File ScoreAfterFlippingMatrix.py


class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        1、保证第一列都是1，这样能保证数最大
            对于每行第一个元素不是1的进行翻转
        2、第一列都是1后再去翻转其他列保证1尽可能的多
        """

        # 遍历矩阵,实现第一步
        for row in grid:
            # print(row)
            if row[0] == 0:  # 行第一个元素为0，进行翻转
                for col in range(len(row)):
                    if row[col] == 0:
                        row[col] = 1
                    else:
                        row[col] = 0
        # 完成第二步
        count_0 = 0  # 每列中0的个数
        count_1 = 0  # 每列中1的个数
        # print(grid)
        for row in range(1, len(grid[0])):  # 将剩余的列转为行再进行计算
            Trans_matrix = [grid[col][row] for col in range(len(grid))]
            # print(Trans_matrix)
            # 遍历转置后的行中1与0的个数，进行对比并转换
            if Trans_matrix.count(1) >= Trans_matrix.count(0):  # 1的个数大于0的个数不用反转
                continue
            else:  # 否则进行反转
                for col in range(len(grid)):
                    if grid[col][row] == 0:
                        grid[col][row] = 1
                    else:
                        grid[col][row] = 0
        # print(grid)
        # 计算二进制
        count =0
        for res in grid:
            Expr = ''
            # print(list(res))
            for i in range(len(res)):
                Expr += str(res[i])
            Expr = '0b' + Expr
            count += eval(Expr)
        print(count)
        return count


if __name__ == '__main__':
    Test = Solution()
    grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    Test.matrixScore(grid)
