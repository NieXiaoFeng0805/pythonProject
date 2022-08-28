# @Time: 2022/8/20 14:46
# @Author: 丨枫
# @File RotateImage.py
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])  # 行和列
        # 创建额外数组
        new_arr = [[0]*row for _ in range(row)]
        for i in range(row):
            for j in range(col):
                # 将每一行元素变为新数组每一列元素
                new_arr[j][col-i-1] = matrix[i][j]
        print(new_arr)
        matrix[:] = new_arr



if __name__ == '__main__':
    Test = Solution()
    Test.rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
