# @Time: 2022/8/1 12:43
# @Author: 丨枫
# @File HightChecker.py
class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = heights.copy()
        expected.sort()
        # print(heights, expected)
        count = 0  # 记录不匹配的次数
        for i in range(len(expected)):
            if expected[i] != heights[i]:  # 出现不匹配
                count += 1
        # print(count)
        return count


if __name__ == '__main__':
    Test = Solution()
    heights = [5, 1, 2, 3, 4]
    Test.heightChecker(heights)
