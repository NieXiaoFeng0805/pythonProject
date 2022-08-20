# @Time: 2022/8/14 11:44
# @Author: 丨枫
# @File MaximumScoreAfterSplittingaString.py
class Solution:
    def maxScore(self, s: str) -> int:
        maxSum = 0

        def count_0(left):
            count = 0
            for i in left:
                if i == '0':
                    count += 1
            return count

        def count_1(right):
            count = 0
            for i in right:
                if i == '1':
                    count += 1
            return count

        for i in range(1, len(s)):
            left, right = s[0:i], s[i:]
            maxSum = max(maxSum, count_1(right) + count_0(left))
        print(maxSum)


if __name__ == '__main__':
    Test = Solution()
    Test.maxScore(s="011101")
