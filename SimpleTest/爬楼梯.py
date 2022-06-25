# @Time: 2022/4/29 14:16
# @Author: 丨枫
# @File 爬楼梯.py
class Solution(object):
    def climbStairs(self, n):

        # n = 3 ; 3种 111;12;21
        # n=4 ； 1111；112；121；211；22  5
        # n=5;11111;1112;1121;1211;2111;212;221;122  8

        # 滚动数组
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n+1):
            temp = first + second
            first = second
            second = temp
        print(second)
        return second
        """
        :type n: int
        :rtype: int
        """


if __name__ == '__main__':
    Test = Solution()
    n = 5
    Test.climbStairs(n)
