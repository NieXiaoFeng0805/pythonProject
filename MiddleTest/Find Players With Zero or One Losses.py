# @Time: 2022/9/8 15:31
# @Author: 丨枫
# @File Find Players With Zero or One Losses.py
from collections import Counter


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:

        # 超时
        """
        # 没有出现在由列表第二个数组成的字典中说明没有败过
        # 在字典中若其值为0则说明只败过一次
        loss_1 = {}
        match_p = set(sum(matches, []))
        print(match_p)
        for i, (j, v) in enumerate(matches):
            if v not in loss_1:
                loss_1[v] = 0
            elif v in loss_1:
                loss_1[v] += 1
        print(loss_1)
        res = [[], []]
        for j in match_p:
            if j not in loss_1:  # 说明没有败过
                res[0].append(j)
            if j in loss_1 and loss_1[j] == 0:  # 败过一次
                res[1].append(j)
        res[0].sort()
        res[1].sort()
        print(res)
        return res"""

        freq = Counter()
        for winner, loser in matches:
            if winner not in freq:
                freq[winner] = 0
            freq[loser] += 1
        print(freq)
        ans = [[], []]
        for key, value in freq.items():
            if value < 2:
                ans[value].append(key)

        ans[0].sort()
        ans[1].sort()
        return ans


if __name__ == '__main__':
    Test = Solution()
    Test.findWinners(matches=[[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]])
