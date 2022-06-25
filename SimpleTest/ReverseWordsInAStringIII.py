# @Time: 2022/5/31 10:18
# @Author: 丨枫
# @File ReverseWordsInAStringIII.py
class Solution:
    def reverseWords(self, s: str) -> str:
        # print(s.split())
        # print(s)
        sList = s.split()
        res = ''
        for i in sList:
            res += i[::-1]+' '
        print(res)
        return res[:(len(res)-1):]
        # 一行
        # return " ".join(word[::-1] for word in s.split(" "))

if __name__ == '__main__':
    Test = Solution()
    s = "Let's take LeetCode contest"
    Test.reverseWords(s)
