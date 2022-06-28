# @Time: 2022/6/27 8:24
# @Author: 丨枫
# @File StringCompression.py
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # 不合要求
        """res = []  # 返回列表
        charDict = {}  # 存放chars中的字符及其个数
        for i in chars:
            charDict[i] = chars.count(i)
        print(charDict)
        for j in charDict:
            if charDict.get(j) == 1:  # 只有一个
                res.append(j)
            else:  # 含多个相同字符
                res.append(j)
                res.append(str(charDict.get(j)))
        print(res)
        return len(res)"""
        # 同上
        """res = [chars[0]]  # 初始化返回列表
        if chars.count(chars[0]) > 1:  # 第一个字符就重复
            res.append(str(chars.count(chars[0])))
        for i in range(1, len(chars)):
            if chars.count(chars[i]) == 1:  # 只有一个
                res.append(chars[i])
            else:  # 重复情况
                if chars[i] == chars[i - 1]:  # 相同的跳过
                    continue
                res.append(chars[i])
                res.append(str(chars.count(chars[i])))
        chars = res
        print(chars)
        return len(chars)"""

        # 用双指针来记录字符串下标，当前指针大于等于数组长度时跳出
        # 当后指针小于数组长度并且是重复字符时，后指针向后移动
        # 碰到新的字符后，将字符存入，游标向右移，进入判断数目
        # 若超过9个则进行拆分
        res = 0  # 返回长度
        charsLength = len(chars)
        pre, last = 0, 1  # 双指针
        while pre < charsLength:
            while last < charsLength and chars[last] == chars[pre]:
                last += 1
            chars[res] = chars[pre]  # 将前指针指向的位置变为字符
            res += 1  # 该字符的下一个位置
            if last - pre > 1:  # 中间间隔多少个的字符，若大于9则进行拆分
                for i in str(last - pre):
                    chars[res] = i
                    res += 1
            pre = last  # 下一段位置
        return res


if __name__ == '__main__':
    Test = Solution()
    chars = ["a", "a", "a", "b", "b", "a", "a"]
    Test.compress(chars)
