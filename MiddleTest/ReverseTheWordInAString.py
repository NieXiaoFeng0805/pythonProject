# @Time: 2022/5/16 10:05
# @Author: 丨枫
# @File ReverseTheWordInAString.py
import self as self


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        Res = ' '
        print(s.split())
        SList = s.split()
        SList.reverse()
        print(SList)
        Res = Res.join(SList)
        print(Res)
        return Res


if __name__ == '__main__':
    Test = Solution()
    s = "the sky is blue"
    Test.reverseWords(s)
