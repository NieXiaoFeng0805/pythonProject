# @Time: 2022/6/30 10:38
# @Author: 丨枫
# @File PrimeArrangements.py
import math as m

import itertools as iters


class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 需要对1~n个数中的质数和非质数进行排列组合
        # 即在质数位上对质数进行排列组合，在非质数位上进行非质数的排列组合

        def isPrime(n):  # 判断是否是质数
            if n == 2 or n == 3:
                return 1
            for i in range(2, int(m.sqrt(n)) + 1):
                if n % i == 0:  # 非质数
                    return 0
            return 1

        # thePrime = []  # 质数列表
        # notPrime = [1]  # 非质数列表
        p = 0  # 质数个数
        np = 1  # 非质数个数
        for i in range(2, n + 1):
            if isPrime(i):
                p += 1
            else:
                np += 1
        print(p, np)
        # 进行全排列
        res = m.factorial(p) * m.factorial(np)
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    n = 5
    Test.numPrimeArrangements(n)
