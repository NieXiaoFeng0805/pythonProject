# @Time: 2022/4/27 15:42
# @Author: 丨枫
# @File 实现strStr.py
class Solution(object):
    def strStr(self, haystack, needle):

        if (needle or haystack) == "":
            return 0
        r_index = haystack.find(needle)
        print(r_index)
        return r_index
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """


if __name__ == '__main__':
    Test = Solution()
    haystack = ''
    needle = ''
    Test.strStr(haystack, needle)
