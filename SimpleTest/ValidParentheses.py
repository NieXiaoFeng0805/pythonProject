# @Time: 2022/5/11 9:51
# @Author: 丨枫
# @File ValidParentheses.py
class Solution(object):
    # def isValid(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     # 括号总数必为偶数个
    #     if len(s) % 2 != 0:
    #         return False
    #     # 判断括号位置
    #     s_list = list(s)
    #     s_listLength = len(s_list)
    #     # print(s_list)
    #     # 将所有对称的括号找到并删除对称的另一个
    #     for i in range(s_listLength):
    #         if i < s_listLength:
    #             if s_list[i] == '(':
    #                 while i + 1 < s_listLength:
    #                     if s_list[i + 1] == ')':
    #                         s_list.pop(i + 1)
    #                         break
    #                     i+=1
    #             if s_list[i] == '[':
    #                 while i + 1 < s_listLength:
    #                     if s_list[i + 1] == ']':
    #                         s_list.pop(i + 1)
    #                         break
    #                     i += 1
    #             if s_list[i] == '{':
    #                 while i + 1 < s_listLength:
    #                     if s_list[i + 1] == '}':
    #                         s_list.pop(i + 1)
    #                         break
    #                     i += 1
    #         s_listLength = len(s_list)
    #     print(s_list)
    #     # 如果剩下的括号中还有另外一半就是无效的
    #     for j in s_list:
    #         if j == ')' or j == ']' or j == '}':
    #             print("False")
    #             return False
    #     print("True")
    #     return True

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 括号总数必为偶数个
        if len(s) % 2 != 0:
            return False
        # 将匹配的括号用空白字符代替，如果最后为 ’‘ 则证明是有效的
        # 最多循环1/2长度的次数
        for i in range(len(s) // 2):
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
        # 判断是否为空
        if s == '':
            print("True")
            return True
        else:
            print("False")
            return False


if __name__ == '__main__':
    Test = Solution()
    s = "()[{]}"
    Test.isValid(s)
