# @Time: 2022/7/29 23:11
# @Author: 丨枫
# @File Dota2Senate.py
import collections


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = [i for i in senate]
        # print(senate)
        count_R, count_D = collections.deque(), collections.deque()  # 计算各方议员数
        print(count_R, count_D)
        for i, v in enumerate(senate):
            if v == 'R':  # R阵营
                count_R.append(i)
            else:  # D 阵营
                count_D.append(i)
        while count_D and count_R:  # 直到有一方终止
            if count_R[0] < count_D[0]:  # R阵营在前面
                count_R.append(count_R[0] + len(senate))
            else:
                count_D.append(count_D[0] + len(senate))
            count_R.popleft()
            count_D.popleft()
        return "Radiant" if count_R else "Dire"

if __name__ == '__main__':
    Test = Solution()
    senate = "RDDRDRDRDRDRDRDRDRDRDRDR"
    Test.predictPartyVictory(senate)
