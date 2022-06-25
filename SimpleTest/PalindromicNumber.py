# @Time: 2022/4/16 11:04
# @Author: 丨枫
# @File PalindromicNumber.py
from xml.etree.ElementTree import tostring

class Solution(object):
    def isPalindrome(self, x):
        # 转为字符串
        Str = str(x)
        lst = list(Str)
        # 对列表进行反转操作,reverse()返回为None
        lst.reverse()
        # 判断是否相同
        return ''.join(lst)==Str
if __name__ == '__main__':
    test = Solution()
    a = 12321
    test.isPalindrome(a)

