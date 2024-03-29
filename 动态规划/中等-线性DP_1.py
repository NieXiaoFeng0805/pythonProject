# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/18 18:42
# software: PyCharm
"""
文件说明：
给出一个数组num，其中num[i]表示第i个位置上有多少钱
要求：能取出的最高金额（取出的位置不能相邻）

例： [1,2,3,1]
输出： 4；  取 1和3 最大


进阶： 数组收尾相连，其他要求保持不变，求取出的最高金额
例子： [2,3,2]  输出：3 （只能拿中间的，首尾相邻）
"""


class Solution:
    def solution(self, num_list):
        n = len(num_list)
        dp = [-1] * (n + 1)  # dp[i] 表示到 第i个元素为止，能取到的最大值
        dp[0] = num_list[0]
        dp[1] = max(num_list[0], num_list[1])

        for i in range(2, n):
            # 第i个 的最大取值 为 前i-2个元素的最大值+第i个元素的和；
            # 若 第i个 元素不取，则为前i-1个元素的和
            dp[i] = max(dp[i - 1], dp[i - 2] + num_list[i])
        return dp[n - 1]


Solution().solution([1, 2, 3, 1])
