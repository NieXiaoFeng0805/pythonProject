# @Time: 2022/5/18 19:19
# @Author: 丨枫
# @File ReverseString.py
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # 双指针
        left = 0
        right = len(s) - 1

        while left <= right:
            temp = s[right]
            s[right] = s[left]
            s[left] = temp
            right -= 1
            left += 1
        # print(s)


if __name__ == '__main__':
    Test = Solution()
    s = ["H", "a", "n", "n", "a", "h"]
    Test.reverseString(s)
