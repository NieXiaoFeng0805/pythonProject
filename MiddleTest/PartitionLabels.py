# @Time: 2022/6/25 11:01
# @Author: 丨枫
# @File PartitionLabels.py
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
            # 用字典存储所有S中的字符以及其最后出现的位置，即键为字符，值为下标
            # 再次遍历，每遍历一个字符计数器+1，再当前字符最后出现的下标比初始设定的下标大时说明后面还有相同的字符，将右下标更新；
            # 若当前字符下标等于设置下标时说明这段已经结束了，将计数器结果存入列表，随后清零

        alphaDict = {}
        for v, k in enumerate(s):  # 创建字典
            alphaDict[k] = v
        print(alphaDict)
        num = 0  # 计数器
        res = []  # 返回列表
        # print(alphaDict[s[0]])
        right = alphaDict[s[0]]  # 初始化右下标,第一个字符的最后出现位置
        for i in range(len(s)):
            num += 1  # 遍历一个计数器+1
            if alphaDict[s[i]] > right:  # 最后的位置比刚才大，则更新位置
                right = alphaDict[s[i]]
            if i == right:  # 这一段子字符串找完了
                res.append(num)  # 这一段的长度
                num = 0  # 计数器清零
        print(res)
        return res

if __name__ == '__main__':
    Test = Solution()
    s = "ababcbacadefegdehijhklij"
    Test.partitionLabels(s)
