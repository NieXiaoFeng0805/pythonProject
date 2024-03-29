# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/3 11:28
# software: PyCharm
"""
文件说明：

"""

'''
1. 确定DP数组
采用布尔类型的dp数组 dp[i][j]  区间范围[i,j](左闭右闭)是否是回文子串;若是,则dp[i,j] = true, 否则为False

2. 确定递推公式
    i. s[i] != s[j]  dp[i][j] = False
    ii. s[i] == s[j]  
        一. 下标i,j相同, 即同一个字符,必然是回文子串  dp[i][j] = True
        二. 下标i,j相差 1和2 时, 例如 aa 和 aba 都是回文子串  dp[i][j] = True
        三. 下标i,j相差大于2 时, 需要判断[i,j]区间内的字符串是不是回文
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        max_len = 1
        begin = 0
        dp = [[False] * n for _ in range(n)]
        print(dp)
        # 下标位置相同必定是回文子串
        for i in range(n):
            dp[i][i] = True
        # 先枚举子串的长度
        for l in range(2, n + 1):
            # 枚举左边界
            for i in range(n):
                j = l + i - 1  # 确定右边界
                if j >= n:  # 右边界越界,跳出当前循环
                    break
                if s[i] != s[j]:  # 两边界不等, 必然不是回文子串,设为False
                    dp[i][j] = False
                else:  # 边界相等的两种情况
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 只要dp[i][l] == True 成立 ,表示s[i..l]是回文子串
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i  # 最长回文子串的初始下标
        return s[begin:begin + max_len]


# 确定dp数组

if __name__ == '__main__':
    S = Solution()
    S.longestPalindrome(s="babad")
    # S.longestPalindrome(s="babadasdfghfghdasfggfs")
