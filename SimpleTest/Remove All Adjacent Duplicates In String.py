# @Time: 2022/9/5 14:45
# @Author: 丨枫
# @File Remove All Adjacent Duplicates In String.py
class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 1
        while i < len(s):
            if s[i] == s[i - 1]:
                rep = s[i - 1:i + 1]
                s = s.replace(rep, "")  # 将该重复全部替换
                i = i - 1 if i != 1 else i - 0
                continue
            i += 1
        print(s)
        return s


if __name__ == '__main__':
    Test = Solution()
    Test.removeDuplicates(s="aababaab")
