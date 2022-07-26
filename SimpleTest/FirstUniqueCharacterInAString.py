# @Time: 2022/7/25 20:10
# @Author: 丨枫
# @File FirstUniqueCharacterInAString.py
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 构建字典，存储该字符出现的次数
        alphaDict = dict(zip(list(i for i in s), list(0 for _ in s)))
        print(alphaDict)
        for i in s:  # 出现的字符则加1
            alphaDict[i] += 1
        print(alphaDict)
        for j in alphaDict:  # 遍历字典，之间返回第一个值为1的对应字符串的下标
            if alphaDict[j] == 1:
                print(s.index(j))
                return s.index(j)
        return -1


if __name__ == '__main__':
    Test = Solution()
    s = "loveleetcode"
    Test.firstUniqChar(s)
