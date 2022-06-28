# @Time: 2022/6/26 19:50
# @Author: 丨枫
# @File IsSubSequence.py


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 若s中有一个不在t中则直接返回
        # 若s中都字符都在t中，则需要分情况
        # 一是按顺序的，返回True；一种是错位的，返回False；考虑如何判断是否错位即可
        # 每找到一个就将其下标记录，遍历结束后判断下标是否升序即可

        # 包含子串
        if s in t:
            return True

        indexList = []
        # 需要删除才能包含
        for index, val in enumerate(s):
            if val not in t:  # 子串有字符不在母串中
                return False
            if s.count(val) > t.count(val):  # 子串中的重复项大于母串
                return False
            if val in t:  # 记录下标
                indexList.append(t.find(val))
        # 判断是否升序
        print(indexList)
        judgeList = []
        # 保留顺序并去重
        for i in range(len(indexList)):
            if indexList[i] not in judgeList:
                judgeList.append(indexList[i])
        print(judgeList)
        for j in range(1, len(judgeList)):
            if indexList[j] < indexList[j - 1]:  # 出现降序
                return False
        return True


if __name__ == '__main__':
    Test = Solution()
    s = "leeeeetcode"
    t = "yyyyylyyeyyyyyeyyeyyeyyeyyeyyytyycyyotttdttttettt"
    Test.isSubsequence(s, t)
