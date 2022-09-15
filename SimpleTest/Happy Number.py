# @Time: 2022/9/13 19:47
# @Author: 丨枫
# @File Happy Number.py
class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        n_list = [i for i in s]
        repeat = [0]
        while repeat[-1] < 2**31:
            res = 0
            for i in n_list:
                res += int(i) ** 2
            if res in repeat:
                return False
            if res == 1:
                return True
            repeat.append(res)
            temp = str(res)
            n_list = [i for i in temp]
        return False


if __name__ == '__main__':
    Test = Solution()
    Test.isHappy(n=2)
