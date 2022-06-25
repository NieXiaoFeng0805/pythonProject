# @Time: 2022/6/24 15:58
# @Author: 丨枫
# @File ValidPalindromeII.py
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """# # 三种情况，一种是直接为回文串，返回True；二是差一个即可为回文串；三是差了不止一个
        # # 若是差一个，观察字符串中奇数项最多有两个；两个及以上则不可为回文串
        # alphatable = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
        #               't', 'u', 'v', 'w', 'x', 'y', 'z']
        # if s == s[::-1]:
        #     return True
        # count = 0  # 计算奇数项的个数
        # theindex = 0  # 一个字符的奇数项下标
        # for i in alphatable:
        #     num = s.count(i)
        #     if num % 2 != 0:
        #         count += 1
        #     if num == 1:
        #         theindex = s.index(i)
        #
        # # 特殊情况奇数项的位置,有两个奇数项且两个都不在中间则返回False，有一个在中间则返回True
        # if count == 2:
        #     index = len(s) // 2
        #     if s.count(s[index]) == 1:  # 中间位置为奇数项且只有1个字符
        #         return True
        #     if s.count(s[len(s) // 2 - 1]) != 1:  # 单个字符项不在中间,删除单个的后判断能不能
        #         # print(s.replace(s[theindex],''))
        #         ss = s.replace(s[theindex], '')
        #         if ss == ss[::-1]:
        #             return True
        #         else:
        #             return False
        #     # 两个字符都是单个且都不在中间
        #     if s.count(s[len(s) // 2 - 1]) % 2 == 0:
        #         return False
        # if count > 2:  # 超过两个奇数项
        #     return False
        # else:
        #     return True"""

        # 从两边向中间进行遍历，对比，若遇到不同的字符则将其删除后再进行对比
        if s == s[::-1]:
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:  # 左右相等时
                left += 1
                right -= 1
            else:  # 左右不等时
                sl = s[:left] + s[left + 1:]  # 删左边
                sr = s[:right] + s[right + 1:]  # 删右边
                # 判断是否回文
                if sl == sl[::-1]:
                    ss = sl
                    break
                elif sr == sr[::-1]:
                    ss = sr
                    break
                else:
                    return False
        return ss == ss[::-1]

if __name__ == '__main__':
    Test = Solution()
    s = "abca"
    print(len(s))
    Test.validPalindrome(s)
