# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/18 18:17
# software: PyCharm
"""
文件说明：
给出非负整数 num ，返回将其变0所需要的步数
要求： 偶数则除以2； 奇数则-1

例子： num=14， 输出；6
"""


class Solution:
    def solution(self, num: int):
        # dp[i]表示 i 变成0的步数
        dp = [-1] * (num + 1)  # 状态数组
        dp[0] = 0
        for i in range(1, num):
            if i % 2 != 0:  # 奇数
                dp[i] = dp[i - 1] + 1  # 若i是奇数，则 i 到 0 的步数是 i-1 到 0 的步数 +1
            else:
                dp[i] = dp[i // 2] + 1  # 若i是偶数，则 i 到 0 的步数是 i//2 到 0 的步数 +1
        return dp[num]


Solution().solution(14)
