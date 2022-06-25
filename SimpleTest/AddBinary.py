# @Time: 2022/5/12 10:09
# @Author: 丨枫
# @File AddBinary.py
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 将字符串转为二进制再转整数,int第二个参数是进制类型，默认10进制
        AddRes = int(a, 2) + int(b, 2)
        # 再转二进制
        AddRes = bin(AddRes)
        #把前面的0b去掉
        AddRes = AddRes[2::]
        #转字符串
        AddRes = str(AddRes)
        print(AddRes)
        return AddRes


if __name__ == '__main__':
    Test = Solution()
    a = "1"
    b = "111"
    Test.addBinary(a, b)
