# @Time: 2022/5/18 20:37
# @Author: 丨枫
# @File ReverseVowelsOfAString.py
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        tempList = []
        V_index = []
        vowels = ['a', 'e', 'i', 'o', 'u']
        # 找到字符串中的元音字母及其下标并存储
        for i in range(len(s)):
            for j in vowels:
                if s[i].lower() == j or s[i].upper == j:
                    tempList.append(s[i])
                    V_index.append(i)
        # 将元音字母反转
        tempList.reverse()
        print(tempList)
        s = list(s)
        # 打包成字典
        indexDict = dict(zip(V_index, tempList))
        # 遍历并替换
        for k in indexDict:
            print(k)
            s[k] = indexDict.get(k)
        new_s = ''.join(s)
        print(new_s)
        return new_s


if __name__ == '__main__':
    Test = Solution()
    s = "Ui"
    Test.reverseVowels(s)
