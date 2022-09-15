# @Time: 2022/9/5 13:38
# @Author: 丨枫
# @File Occurrences After Bigram.py
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        str_list = text.split(' ')
        n = len(str_list)
        res = []
        """l, r = 0, 1
        print(str_list)
        while r < n:
            if str_list[l] == first and str_list[r] == second:
                temp = r + 1
                if temp < n:
                    res.append(str_list[temp])
            l += 1
            r += 1
        print(res)
        return res"""
        for i in range(2, n):
            if str_list[i - 2] == first and str_list[i - 1] == second:
                res.append(str_list[i])
        return res


if __name__ == '__main__':
    Test = Solution()
    Test.findOcurrences(text="alice is a good girl she is a good student", first="a", second="good")
