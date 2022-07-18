# @Time: 2022/7/10 15:23
# @Author: 丨枫
# @File MaximalRectangle.py
import numpy as np
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        print(matrix)
        print(np.mat(matrix))

if __name__ == '__main__':
    Test = Solution()
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    Test.maximalRectangle(matrix)
