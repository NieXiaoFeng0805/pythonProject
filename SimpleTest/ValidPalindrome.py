# @Time: 2022/5/7 13:11
# @Author: 丨枫
# @File ValidPalindrome.py
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 转为字符串并合并
        a = ''.join(e for e in s if e.isalnum())
        # 转小写
        a = a.lower()
        # 反转字符串
        b = list(a)
        b.reverse()
        c = ''.join(b)
        # print(c)
        # 判断是否回文
        if c == a:
            return True


if __name__ == '__main__':
    Test = Solution()
    s = "A man, a plan, a canal: Panama"
    Test.isPalindrome(s)
