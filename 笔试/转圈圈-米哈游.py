# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/17 10:23
# software: PyCharm
"""
文件说明：
数组长度为n，hi表示每个数
存在数E使得全体n-E，若 hi<=50% 则再次 n-R 每次n-R后需要更新次数
"""


#
# class Solution:
#     def create_num(self):
#         T = int(input())
#         num_list = []
#         n, E, R = [], [], []
#         for i in range(T):
#             n.append(int(input()))
#             num_list.append([int(x) for x in input().split()])
#             e, r = [int(x) for x in input().split()]
#             E.append(e)
#             R.append(r)
#         return num_list, n, E, R
#
#     def damE(self, num_list: list, E):
#         n = len(num_list)
#         cnt_R = 0
#         tar_list = []
#         for i in range(n):
#             tmp = num_list[i] // 2
#             tar_list.append(tmp)
#             num_list[i] -= E
#             if 0 < num_list[i] <= tmp:
#                 cnt_R += 1  # 转圈圈+1
#         return num_list, cnt_R, tar_list
#
#     def damR(self, num_list: list, R: int, cnt_R: int, tar: list):
#         n = len(num_list)
#         add_cnt_r = 0
#         for i in range(n):
#             if add_cnt_r:
#                 cnt_R += add_cnt_r
#             num_list[i] -= R * cnt_R
#             if num_list[i] <= tar[i]:
#                 add_cnt_r += 1
#
#         return num_list, cnt_R
#
#     def judge_zero(self, num_list: list):
#         cnt = 0
#         n = len(num_list)
#         for num in num_list:
#             if num <= 0:
#                 cnt += 1
#         if cnt == n:
#             return True
#         else:
#             return False
#
#     def solution(self):
#         num_list, N, E, R = self.create_num()
#         cnt_E, cnt_R = 0, 0
#         n = len(num_list)
#
#         # 每一组数据
#         for i in range(n):
#             sub_num = num_list[i]  # 当前数组
#             n = N[i]  # 每组数据多少个
#             e = E[i]  # 主动伤害
#             r = R[i]  # 被动伤害\
#
#             while True:
#                 sub_num, cnt_R, tar_list = self.damE(sub_num, e)  # 使用E
#                 cnt_E += 1
#                 while cnt_R != 0:  # 开始追击
#                     sub_num, cnt_R = self.damR(sub_num, r, cnt_R, tar_list)
#                 # 判断全部为0
#                 flag = self.judge_zero(sub_num)
#                 if flag:
#                     print(str(cnt_E) + ' ' + str(cnt_R))
#                     break


class Solution:
    def main_func(self):
        '''
        主函数
        :return:
        '''
        # 共T组数据   所有数组列表、数组长度数组、E伤害数组、R伤害数组
        T, num_list, N, E, R = self.create_num()
        # 每组到50%的 数组
        tar_list = self.get_targetList(num_list)
        # 记录E和R的次数
        cnt_E, cnt_R = 0, 0

        # 对每个数组来说，先用一次E->计算使用R的次数->使用R->每使用一次就判断当前数组是否全部<=0
        # 若没有<=0 :则继续使用R, 直到次数用完后, 再次使用E, 重复上述操作
        # 若全部 <=0 ,则返回cnt_E和cnt_R

        for t in range(T):  # 共T组数据
            n, sub_list, e, r = N[t], num_list[t], E[t], R[t]
            tarl = tar_list[t]
            while True:
                # 使用一次E
                cnt_E += 1
                flag, sub_list, cur_r, index_curR = self.damage_E(sub_list, tarl, e)
                # 结束
                if flag:  # 全部归0
                    print(str(cnt_E) + ' ' + str(cnt_R))
                    break
                # 判断是否追击
                if cur_r != 0:
                    flag, cnt_R = self.damage_R(sub_list, tarl, index_curR, r, cur_r, cnt_R)
                # 结束
                if flag:  # 全部归0
                    print(str(cnt_E) + ' ' + str(cnt_R))
                    break

    def damage_R(self, num_list: list, target_list: list, index_curR: list, R: int, cur_r: int, cnt_R: int):
        '''
        计算追击后剩余的情况,每追击一次更新以下状态
        若 有新的50%以下,则更新下标后继续追击,每次追击完判断是否全部<=0
        :param num_list:
        :param target_list:
        :param R:
        :return:
        '''
        cnt_R = cur_r
        n = len(num_list)
        flag = False
        while cur_r > 0:  # 追击次数
            for i in range(n):
                num_list[i] -= R  # 追击伤害
                if num_list[i] <= target_list[i] and i not in index_curR:  # 出现新的追击
                    cur_r += 1  # 循环次数+1
                    cnt_R += 1  # R的次数+1
                    index_curR.append(i)
            cur_r -= 1  # 每追击一次,cur_r -1
            # 每追击一次判断是否全部归0
            flag = self.judge_zero(num_list)
            if flag:  # 全部归0
                break
        return flag, cnt_R

    def judge_zero(self, num_list):
        for i in num_list:
            if i > 0:
                return False
        return True

    def damage_E(self, num_list: list, target_list: list, E: int):
        '''
        计算E的伤害后的数组,
        :param num_list:
        :param E:
        :return:
        '''
        cur_r = 0  # 追击次数
        index_curR = []  # 记录需要追击的下标
        n = len(num_list)
        for i in range(n):
            num_list[i] -= E
            if num_list[i] <= target_list[i]:  # 到50%及以下
                cur_r += 1
                index_curR.append(i)
        flag = self.judge_zero(num_list)
        return flag, num_list, cur_r, index_curR

    def create_num(self):
        T = int(input())
        num_list = []
        n, E, R = [], [], []
        for i in range(T):
            n.append(int(input()))
            num_list.append([int(x) for x in input().split()])
            e, r = [int(x) for x in input().split()]
            E.append(e)
            R.append(r)
        return T, num_list, n, E, R

    def get_targetList(self, num_list):
        '''
        获取触发条件数组
        :param sub_list:
        :return:
        '''
        target_list = []
        for i in num_list:
            target_list.append([x // 2 for x in i])
        return target_list


Solution().main_func()
# 3
# 5
# 100 50 60 80 70
# 25 10
# 5
# 100 50 60 80 70
# 20 20
# 5
# 100 200 300 4000 5000
# 50 1000