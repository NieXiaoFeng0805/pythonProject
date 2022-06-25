# @Time: 2022/5/24 9:26
# @Author: 丨枫
# @File IsomorphicStrings.py

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # print(set(s))
        # 若字符串转为集合后长度不相同则不同构
        if len(set(s)) != len(set(t)):
            # print("False")
            return False
        # 长度相同映射关系不同也不同构
        for i in range(len(s)):
            # print(s.index(s[i]))
            # print(t.index(t[i]))
            if s.index(s[i]) != t.index(t[i]):
                return False
        return True

if __name__ == '__main__':
    Test = Solution()
    s = "paper"
    t = "titll"
    Test.isIsomorphic(s, t)