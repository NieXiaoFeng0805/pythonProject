# @Time: 2022/7/12 22:44
# @Author: 丨枫
# @File MaximumNestingDepthOfTheParentheses.py
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 从左往右遍历，记录左括号的最大次数
        # 遍历字符串，遇到左括号则计数器+1；遇到右括号则计数器-1

        count = 0  # 计数
        Max_count = 0
        for i in s:
            if i == '(':
                count += 1
            if i == ')':
                count -= 1
            Max_count = max(count, Max_count)
        print(Max_count)
        return Max_count


if __name__ == '__main__':
    Test = Solution()
    s = "8*((1*(5+6))*(8/6))"
    Test.maxDepth(s)
