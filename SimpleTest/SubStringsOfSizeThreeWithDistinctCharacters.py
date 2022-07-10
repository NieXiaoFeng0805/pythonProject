# @Time: 2022/7/7 13:57
# @Author: 丨枫
# @File SubStringsOfSizeThreeWithDistinctCharacters.py
class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 3:
            return 0
        L, R = 0, 2  # 左右边界
        res = 0  # 结果
        while R < len(s):
            if s[L] != s[L + 1] and s[L] != s[R] and s[L + 1] != s[R]:
                res += 1
            R += 1
            L += 1
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    s = "xyzzaz"
    Test.countGoodSubstrings(s)
