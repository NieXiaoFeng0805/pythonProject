# @Time: 2022/9/18 17:53
# @Author: 丨枫
# @File Ugly Number.py
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        ugly = [2, 3, 5]
        for factor in ugly:
            while n % factor == 0:
                n //= factor

        return n == 1


if __name__ == '__main__':
    Test = Solution()
    Test.isUgly(n=6)
