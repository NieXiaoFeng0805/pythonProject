# @Time: 2022/5/24 12:31
# @Author: 丨枫
# @File UniqueMorseCodeWords.py


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # 摩斯密码表
        MorseTable = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        # 字母表
        AlphabetTable = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']
        # 映射字典
        AlphaDict = dict(zip(AlphabetTable, MorseTable))
        # 翻译列表
        AlphaList = []
        # print(AlphaDict)
        for i in words:
            s = ''
            for j in range(len(i)):
                # print(i[j])
                # print(AlphaDict.get(i[j]))
                s += ''.join(AlphaDict.get(i[j]))
            AlphaList.append(s)
        # 转集合
        AlphaSet = set(AlphaList)
        print(AlphaSet)
        return len(AlphaSet)


if __name__ == '__main__':
    Test = Solution()
    words = ["gin", "zen", "gig", "msg"]
    Test.uniqueMorseRepresentations(words)
