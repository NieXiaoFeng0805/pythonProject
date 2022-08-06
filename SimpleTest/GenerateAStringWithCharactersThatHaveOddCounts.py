# @Time: 2022/8/1 11:48
# @Author: 丨枫
# @File GenerateAStringWithCharactersThatHaveOddCounts.py
class Solution:
    def generateTheString(self, n: int) -> str:
        """
        if n % 2 != 0:  # n为奇数
            res = ''.join(['a' for i in range(n)])
            print(res)
        else:
            res = ''.join(['a' for i in range(n - 1)]) + 'b'
            print(res)
        """
        # 一行
        return ''.join(['a' for i in range(n)]) if (n % 2 != 0) else''.join(['a' for i in range(n - 1)]) + 'b'

if __name__ == '__main__':
    Test = Solution()
    n = 6
    Test.generateTheString(n)
