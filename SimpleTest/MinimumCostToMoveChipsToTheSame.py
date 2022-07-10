# @Time: 2022/7/8 10:44
# @Author: 丨枫
# @File MinimumCostToMoveChipsToTheSame.py
from turtle import position


class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        # 不全面
        """        
        # 移动到筹码最多的那个位置上花费最少
        # 若最大筹码在偶索引且当前遍历为奇索引，则将奇数位的筹码加到上面并cost+其个数
        # 若最大筹码在奇索引且当前遍历为偶索引，则将偶数数位的筹码加到上面并cost+其个数
        # 其余情况无需花费

        # 排个序
        position.sort()
        # 设置字典，键为筹码下标，值为筹码个数
        Chips_dict = {i: position.count(i) for i in position}
        # print(Chips_dict)
        cost = 0  # 花费
        Max_index = max(Chips_dict, key=Chips_dict.get)  # 标识筹码最多位置的索引
        # print(Max_index)

        # 判断筹码最大值所在索引的奇偶
        flag = False
        if Max_index % 2 == 0:  # 为偶
            flag = True
        # 遍历字典
        for chips in Chips_dict:
            if flag and chips % 2 != 0:  # 最大筹码在偶索引且当前遍历为奇索引
                # 将奇数位的筹码加到上面并cost+其个数
                cost += Chips_dict.get(chips)
            if (flag == False) and chips % 2 == 0:  # 最大筹码在奇索引且当前遍历为偶索引
                # 将偶数数位的筹码加到上面并cost+其个数
                cost += Chips_dict.get(chips)
        print(cost)
        return cost
"""

        # 在上面的基础上，可以发现，将position拆成奇偶两部分来看，只要将奇/偶数组中较小的一个全部转移到另外一组上即可
        # 因为筹码移动到最后会变成两组，一组在奇数下标，一组在偶数下标，将较小的部分全部移动的到另一部分代价最小

        Even_num = 0  # 奇数项
        Odd_num = 0  # 偶数项
        # 设置字典，键为筹码下标，值为筹码个数
        Chips_dict = {i: position.count(i) for i in position}
        for i in Chips_dict:
            if (i + 1) % 2 == 0:  # 为奇
                Even_num += Chips_dict.get(i)
            else:
                Odd_num += Chips_dict.get(i)
        print(Even_num, Odd_num)
        return min(Even_num, Odd_num)


if __name__ == '__main__':
    Test = Solution()
    position = [3, 3, 1, 2, 2]
    Test.minCostToMoveChips(position)
