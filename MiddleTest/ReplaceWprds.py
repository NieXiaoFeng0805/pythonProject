# @Time: 2022/7/7 14:35
# @Author: 丨枫
# @File ReplaceWprds.py
class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        # 给字典按长度排序
        new_dict = sorted(dictionary, key=lambda x: len(x))
        # 拆分字符串
        sentence_list = sentence.split(" ")
        # print(dictionary, sentence_list)
        res = []
        flag = True
        for i in sentence_list:
            for j in new_dict:
                if j in i and j[0:len(j)] == i[0:len(j)]:  # 可替换为词根
                    res.append(j)
                    flag = False
                    break
                flag = True
            if flag:  # 当前单词不存在与字典中
                res.append(i)
        print(' '.join(res))
        return ' '.join(res)


if __name__ == '__main__':
    Test = Solution()
    dictionary, sentence = ["catt", "cat", "bat", "rat"], "the cattle was rattled by the battery"
    Test.replaceWords(dictionary, sentence)
