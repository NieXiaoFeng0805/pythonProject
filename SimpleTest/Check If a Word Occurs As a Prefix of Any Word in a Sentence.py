# @Time: 2022/8/21 13:33
# @Author: 丨枫
# @File Check If a Word Occurs As a Prefix of Any Word in a Sentence.py
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        wordList = sentence.split(" ")
        print(wordList)
        for i in wordList:
            if searchWord == i[:len(searchWord)]:
                return wordList.index(i) + 1
        return -1


if __name__ == '__main__':
    Test = Solution()
    Test.isPrefixOfWord(sentence="i love eating burger", searchWord="burg")
