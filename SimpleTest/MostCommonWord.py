# @Time: 2022/5/25 9:57
# @Author: 丨枫
# @File MostCommonWord.py
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # 将标点去掉再转为列表
        # print(paragraph.split())
        for i in paragraph:
            # print(i.isalpha())
            if False == i.isalpha():
                paragraph = paragraph.replace(i, ' ')
        paragraphList = paragraph.split()
        print(paragraphList)
        # 小写
        for a in range(len(paragraphList)):
            paragraphList[a] = paragraphList[a].lower()
        # banned为空
        if len(banned) == 0:
            return paragraphList[0]
        countList = []
        # 找到需要删除的元素
        for v in banned:
            countList.append(paragraphList.count(v))
        maxCount = max(countList)
        # 开始删除
        for j in range(maxCount):
            for k in banned:
                if paragraphList.count(k) !=0:
                    paragraphList.remove(k)
                else:
                    pass
        # print(paragraphList)
        # 开始计算
        countNum = []
        for b in paragraphList:
            countNum.append(paragraphList.count(b))
        # print(countNum)
        # print(countNum.index(max(countNum)))
        # print(paragraphList[countNum.index(max(countNum))])
        return paragraphList[countNum.index(max(countNum))]


if __name__ == '__main__':
    Test = Solution()
    paragraph = "abc abc? abcd the jeff!"
    banned = ["abc", "abcd", "jeff"]
    Test.mostCommonWord(paragraph, banned)
