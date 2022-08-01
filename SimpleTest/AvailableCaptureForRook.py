# @Time: 2022/7/26 16:36
# @Author: 丨枫
# @File AvailableCaptureForRook.py
class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        """
        x_len = len(board)
        y_len = len(board[0])

        R_row, R_col = 0, 0
        count = 0  # 捕获卒的数量
        for row in range(x_len):
            if 'R' in board[row]:
                R_row = row
                R_col = board[row].index('R')

        print(R_row, R_col)
        for up in range(R_row - 1, -1, -1):  # 上方
            if board[up][R_col] == 'p':  # 卒
                count += 1
                break
            if board[up][R_col] == 'B':  # 象
                break
        for dw in range(x_len - R_row):  # 下方
            if board[dw + R_row][R_col] == 'p':  # 卒
                count += 1
                break
            if board[dw + R_row][R_col] == 'B':  # 象
                break
        for l in range(R_col, -1, -1):  # 左方
            if board[R_row][l] == 'p':  # 卒
                count += 1
                break
            if board[R_row][l] == 'B':  # 象
                break
        for r in range(y_len - R_col):  # 右方
            if board[R_row][r + R_col] == 'p':  # 卒
                count += 1
                break
            if board[R_row][r + R_col] == 'B':  # 象
                break
        print(count)
        return count"""

        # 优化
        # 一维展开
        R_row, R_col = 0, 0
        count = 0  # 捕获卒的数量
        for row in range(len(board)):
            if 'R' in board[row]:
                R_row = row
                R_col = board[row].index('R')
        S = ''.join(board[R_row])
        S = S.replace('.', '')
        if 'pR' in S:
            count += 1
        if 'Rp' in S:
            count += 1
        S = ''.join(i[R_col] for i in board)
        S = S.replace('.', '')
        if 'pR' in S:
            count += 1
        if 'Rp' in S:
            count += 1
        return count


if __name__ == '__main__':
    Test = Solution()
    board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]

    Test.numRookCaptures(board)
