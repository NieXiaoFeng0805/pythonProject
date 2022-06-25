# @Time: 2022/4/27 14:06
# @Author: 丨枫
# @File 最长回文子串.py
class Solution(object):
    def longestPalindrome(self, s):
        # 1、先判断整个串是不是回文的
        # 2、整串长度减一再次判断
        # ...
        # StrArr = []
        # # 转列表
        tran_s = list(s)
        # # 遍历
        # for i in range(len(tran_s)):
        #     StrArr
        # # 反转
        # tran_s.reverse()
        # # 拼串
        # new_s = ''.join(tran_s)
        # # print(new_s)
        # # 判断
        # if new_s == s:
        #     return new_s
        # 两下标
        arr = []
        i = 0
        while i < len(s):
            flag = 0
            for j in range(flag, len(tran_s) - flag):
                arr.append(tran_s[j])
            # 反转
            arr.reverse()
            # 拼串
            new_s = ''.join(arr)
            # 判断
            if arr == new_s:
                print(arr)
            else:
                print('不是')
            flag += 1
            i += 1


        print(new_s)

        """
        :type s: str
        :rtype: str
        """


if __name__ == '__main__':
    Test = Solution()
    s = "babad"
    Test.longestPalindrome(s)
