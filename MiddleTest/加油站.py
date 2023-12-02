from typing import List
import collections
from random import choice
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        遍历gas数组，起始gas为0，到下一站[i+1]则减去当前cost[i]，若结果小于0则不能到达下一站
        ——看是否能返回原地
        1、总耗油量大于总汽油量，一定不能到
        2、反之则有唯一解（题目要求）
        '''

        if sum(cost) > sum(gas):
            return -1

        cur_move, sum_move = 0, len(gas)  # 当前移动的步数，总共需要移动的步数
        cur = 0  # 当前站点
        car = 0  # 汽车

        while cur_move < sum_move:
            car = car + gas[cur_move] - cost[cur_move]  # 到下一站时剩余的汽油
            if car < 0:  # 在cur_move处的油量<0，说明从之前站点出发的车均无法到达i.
                cur = cur_move + 1  # 从下一个站点出发
                car = 0  # 清空油箱
            cur_move += 1
        print(cur)
        return cur


# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#
#         '''总油量 < 总耗油量，一定无解'''
#         if sum(gas) < sum(cost):
#             return -1
#
#         '''sum(gas) >= sum(cost)，一定有解【题目保证唯一解】'''
#         n = len(gas)
#         start = 0  # 记录出发点，从索引0开始
#         total = 0  # 记录汽车实际油量
#         for i in range(n):
#             total += gas[i] - cost[i]  # 每个站点加油量相当于 gas[i] - cost[i]
#             if total < 0:  # 在i处的油量<0，说明从之前站点出发的车均无法到达i
#                 start = i + 1  # 尝试从下一个站点i+1重新出发
#                 total = 0  # 重新出发时油量置为0
#
#         return start  # 解是唯一的


S = Solution()
# S.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2])
S.canCompleteCircuit(gas=[5, 1, 2, 3, 4], cost=[4, 4, 1, 5, 1])
