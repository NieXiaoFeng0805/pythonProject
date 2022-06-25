# @Time: 2022/5/20 15:25
# @Author: 丨枫
# @File ReverseStringII.py
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # 转列表操作
        s_List = list(s)
        # 步长设置为2k
        for i in range(0,len(s_List),2*k):
            s_List[i:i+k] = reversed(s_List[i:i+k]) # 反转后赋值
        print(s_List)
        Restr = ''.join(s_List)
        print(Restr)
        return Restr
if __name__ == '__main__':
    Test = Solution()
    s = "abcdefg"
    k = 2
    Test.reverseStr(s, k)
