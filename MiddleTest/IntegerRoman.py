# @Time: 2022/5/9 19:40
# @Author: 丨枫
# @File IntegerRoman.py
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        RomanList = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']  # 存放所有大种类的罗马字串
        NumList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]  # 对应的数字
        ReTurnList = []
        # print(len(NumList))
        # 在所有大种类中遍历
        for i in range(len(RomanList)):
            # 罗马数字除去几个特殊的，其他都是是左边大右边小
            while num >= NumList[i]:
                if num // NumList[i] > 0:  # 大于特定数
                    ReTurnList.append(RomanList[i])
                    num -= NumList[i]
        Rstr = ''.join(ReTurnList)
        return Rstr

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ReTurnNum = 0
        RomanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s)):
            # 除特殊几个之外，罗马数字是从左到右降序的
            # 左边小于右边就减掉左边的，反之则加上
            if i < len(s) - 1 and RomanDict[s[i]] < RomanDict[s[i + 1]]:
                ReTurnNum -= RomanDict[s[i]]
            else:
                ReTurnNum += RomanDict[s[i]]
        # print(ReTurnNum)
        return ReTurnNum

if __name__ == '__main__':
    Test = Solution()
    num = 'MCMXCIV'
    # Test.intToRoman(num)
    Test.romanToInt(num)
