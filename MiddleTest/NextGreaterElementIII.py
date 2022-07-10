# @Time: 2022/7/3 23:27
# @Author: 丨枫
# @File NextGreaterElementIII.py
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        MaxNum = 2147483647
        # 变成字符串
        s = str(n)
        numList = []
        for i in s:
            numList.append(i)
        #  降序排序
        newList = sorted(numList, reverse=True)
        res = int(''.join(newList))
        print(res)
        if res == n:  # 降序后的数与原数相等，则此时已经是最大了
            return -1

        # 找到最大的和第二大的数,

        # 比较大小
        if res > MaxNum:
            return -1
        else:
            return res


if __name__ == '__main__':
    Test = Solution()
    n = 1234
    Test.nextGreaterElement(n)
