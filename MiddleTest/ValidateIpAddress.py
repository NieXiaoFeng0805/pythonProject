# @Time: 2022/5/29 11:08
# @Author: 丨枫
# @File ValidateIpAddress.py
class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """

        # 判断IPv4
        # 1、其中除了 ‘.’之外的符号则无效
        # 2、超过255的无效
        # 3、0x的无效
        # 4、带字母的无效
        # print(queryIP.split('.'))
        def isIPv4(queryIP):
            count = 0
            AlphabetTable = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            PctString = "~!@#$%^&*()_+-*/<>,[]/"  # 标点符号
            for i in queryIP:
                if i in PctString:  # 若字符串中含有除了 ‘.’ 之外的标点，直接返回
                    print("Neither")
                    return False
                    # '.'只能出现3个
                if i == '.':
                    count += 1
                # 带字母的无效
                if i in AlphabetTable:
                    return False
            if count != 3:
                return False
            # 将IP以‘.’拆分
            SplitList = queryIP.split('.')
            print(SplitList)
            # 遍历拆分列表，若不合法的直接返回
            for j in SplitList:
                # print(int(j))
                # 排除0x和空字段的情况
                if (len(j) >= 2 and j[0] == '0') or (len(j) == 0):
                    print("Neither")
                    return False
                # 排除超过范围的情况
                if int(j) > 255 or int(j) < 0:
                    print("Neither")
                    return False
            print("IPv4")
            return True

        # 判断IPv6地址
        # 1、除‘：’之外的标点即为不合法
        # 2、每个字段长度大于4为无效
        # 3、无效字母
        def isIPv6(queryIP):
            count = 0
            AlphabetTable = "0123456789abcdefABCDEF:"
            PctString = "~!@#$%^&*()_+-*/<>,.[]/"  # 标点符号
            for i in queryIP:
                if i in PctString:  # 包含除‘：’之外的标点
                    print("Neither")
                    return False
                # ':'只能出现7次
                if i == ':':
                    count += 1
                # 无效字母
                if i not in AlphabetTable:
                    return False
            if count != 7:
                return False

            SplitList = queryIP.split(':')
            # print(SplitList)
            for j in SplitList:
                if len(j) > 4 or len(j) == 0:  # 格式不符
                    print("Neither")
                    return False
            print("IPv6")
            return True

        # 判断入口
        if len(queryIP) == 15:
            if '.' in queryIP:
                if isIPv4(queryIP) == True:
                    return "IPv4"
                else:
                    return "Neither"
            else:
                if isIPv6(queryIP) == True:
                    return "IPv6"
                else:
                    return "Neither"
        if len(queryIP) > 15:
            if isIPv6(queryIP) == True:
                return "IPv6"
            else:
                return "Neither"
        else:
            if isIPv4(queryIP) == True:
                return "IPv4"
            else:
                return "Neither"


if __name__ == '__main__':
    Test = Solution()
    queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    Test.validIPAddress(queryIP)
