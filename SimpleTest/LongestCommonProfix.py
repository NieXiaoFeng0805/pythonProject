# @Time: 2022/5/7 9:06
# @Author: 丨枫
# @File LongestCommonProfix.py
class Solution(object):
    def longestCommonPrefix(self, strs):
        #判空
        if strs == [""] or strs[0] == "":
            return ""
        for j in strs:
            if j == "":
                return ""
        """
        :type strs: List[str]
        :rtype: str
        """
        #先将最小的和最大的进行比对
        m1 = min(strs)
        m2 = max(strs)
        res = []
        temp = 0
        if len(m1) > len(m2):
            theMin = m2
            theMax = m1
        else:
            theMin = m1
            theMax = m2
        # print(m2)
        #遍历较短的
        for i, v in enumerate(theMin):
            if v == theMax[i]:
                if i - temp > 1:
                    break
                res.append(v)
                temp = i

        res_str = ''.join(res)
        # 判断这个子串在不在另外一个字符串内
        if theMax[0] != theMin[0]:
            return ""
        for i in strs:
            if (str(i).count(res_str)) == 0:
                print(str(i))
                return ""
        print(res_str)
        return res_str


if __name__ == '__main__':
    Test = Solution()
    strs = [""]
    Test.longestCommonPrefix(strs)
