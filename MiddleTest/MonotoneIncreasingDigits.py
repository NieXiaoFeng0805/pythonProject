# @Time: 2022/6/24 17:37
# @Author: 丨枫
# @File MonotoneIncreasingDigits.py
class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 将其转为字符串后遍历，要求为升序，所以第一个出现降序的位置即为需要修改的位置
        # 观察修改后的结果，要尽量往大的靠，所以将第一个出现降序的位置所在的数字减1，再将其后的数字改为9即可
        if n < 10:
            return n
        flag = 0  # 判断是否出现降序
        s = str(n)
        for i in range(1, len(s)):
            if s[i] < s[i - 1]:  # 出现降序
                # 找到最开始出降序的位置(包括前面相等的数字 )并将其转为整型后减一
                index = s.index(s[i - 1])
                flag = 1
                break
        if flag == 0:
            return n
        resList = list(s)
        resList[index] = str(int(resList[index]) - 1)
        # 后面的位置变为9
        for j in range(index+1,len(resList)):
            resList[j] = '9'
        print(int(''.join(resList)))
        return int(''.join(resList))


if __name__ == '__main__':
    Test = Solution()
    n = 984443
    Test.monotoneIncreasingDigits(n)
