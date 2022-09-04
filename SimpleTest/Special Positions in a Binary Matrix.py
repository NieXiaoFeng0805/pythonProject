# @Time: 2022/9/4 12:14
# @Author: 丨枫
# @File Special Positions in a Binary Matrix.py
class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        row, col = len(mat), len(mat[0])  # 获取行和列
        count = 0
        for r in range(row):
            if mat[r].count(1) > 1:  # 这一行不止一个1
                continue
            for c in range(col):
                if mat[r][c] == 1:
                    temp = 0
                    count_1 = 0
                    while temp < row:
                        if mat[temp][c] == 1:
                            count_1 += 1
                        temp += 1
                    if count_1 > 1:  # 这一列不止一个1
                        break
                    else:
                        count += 1
        print(count)
        return count


if __name__ == '__main__':
    Test = Solution()
    Test.numSpecial(mat=[[1, 0, 0],
                         [0, 0, 1],
                         [1, 0, 0]])
