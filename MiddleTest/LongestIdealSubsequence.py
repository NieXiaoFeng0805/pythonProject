# @Time: 2022/8/13 12:36
# @Author: 丨枫
# @File LongestIdealSubsequence.py
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        f = [0] * 26
        for c in s:
            c = ord(c) - ord('a')
            f[c] = 1 + max(f[max(c - k, 0): c + k + 1])
        return max(f)

if __name__ == '__main__':
    Test = Solution()
    Test.longestIdealString(s="acfgbd", k=2)
