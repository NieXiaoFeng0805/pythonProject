# @Time: 2022/6/27 11:32
# @Author: 丨枫
# @File GreatestEnglishLetterInUpperAndLowerCase.py
class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 先对原串进行降重，创建两个列表，用于存放小写字母和转为小写字母的大写字母
        # 对原串进行遍历，将对于小/大写存入列表
        # 对原串再次遍历，若小写字母出现在两个列表中，则将其转为大写字母添加到结果列表中
        # 返回结果列表最大值，若结果列表为空则返回“”

        s = set(s)  # 降重
        upList = []  # 存放大写字母
        lowList = []  # 存放小写字母
        for i in s:
            if i.islower():
                lowList.append(i)
            else:  # 将大写字母转小写
                upList.append(i.lower())
        res = []  # 存入结果
        for i in s:  # 再次遍历，若该小写字母出现在两端则说明是最好字母
            if i in upList and i in lowList:
                res.append(i.upper())
        if len(res) == 0:
            return ""
        return max(res)


if __name__ == '__main__':
    Test = Solution()
    s = "lEeTcOdE"
    Test.greatestLetter(s)
