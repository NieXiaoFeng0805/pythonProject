# @Time: 2022/5/20 13:54
# @Author: 丨枫
# @File RansomNote.py
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # 全部转为列表之后，遍历一个就移除一个，若移除异常则说明没有，返回False
        ransomNoteList = list(ransomNote)
        magazineList = list(magazine)
        try:
            for i in range(len(ransomNoteList)):
                magazineList.remove(ransomNoteList[i])
            print("True")
            return True
        except:
            print("False")
            return False



if __name__ == '__main__':
    Test = Solution()
    ransomNote = "fihjjjjei"
    magazine = "hjibagacbhadfaefdjaeaebgi"
    Test.canConstruct(ransomNote, magazine)
