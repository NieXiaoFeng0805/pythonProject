# @Time: 2022/5/7 12:00
# @Author: 丨枫
# @File LengthOfTheLastWord.py
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 对字符串进行切片
        newList = s.split()
        print(len(newList[len(newList) - 1]))
        MaxLength = len(newList[len(newList) - 1])
        return MaxLength


if __name__ == '__main__':
    Test = Solution()
    s = "Hello World"
    Test.lengthOfLastWord(s)
