# @Time: 2022/6/25 12:35
# @Author: 丨枫
# @File LemonadeChange.py
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # # 需要找钱的项可设置为5和15美分 ，若完成找零，都需有5这个数；设置找零列表
        # # 遍历bills，若是5则+，10则将5弹出一个再添加，20则有两种情况且20无法用于找零
        # # 若是20，列表中有10 和5则弹出后再继续遍历，若只有5，则判断若5的个数小于3则直接返回
        #
        # total_money = []  # 收入
        # for i in bills:
        #     if i == 5:
        #         total_money.append(i)
        #     if i == 10:  # 需找零
        #         if 5 in total_money:
        #             total_money.remove(5)
        #             total_money.append(10)
        #         else:  # 无法找零
        #             return False
        #     if i == 20:
        #         if sum(total_money) < 15:  # 零钱不够
        #             return False
        #         if 5 not in total_money:
        #             return False
        #         if 10 in total_money and 5 in total_money:  # 找零
        #             total_money.remove(5)
        #             total_money.remove(10)
        #             continue
        #         if 10 not in total_money:
        #             if total_money.count(5) < 3:
        #                 return False
        #             else:  # 找零
        #                 total_money.remove(5)
        #                 total_money.remove(5)
        #                 total_money.remove(5)
        # print("True")
        # return True

        """
        优化：因为是按顺序收钱的，所以记录5、10两种币的个数，当需要找零的时候进行加减即可
        """
        five, ten = 0, 0
        for i in bills:
            if five < 0 or ten < 0:
                return False
            if i == 5:
                five += 1
            if i == 10:
                five -= 1
                ten += 1
            if i == 20:
                if five == 0:
                    return False
                if ten > 0:
                    ten -= 1
                    five -= 1
                    continue
                if ten == 0 and five > 3:
                    five -= 3
                else:
                    return False

        return True


if __name__ == '__main__':
    Test = Solution()
    bills = [5, 5, 5, 10, 20]

    Test.lemonadeChange(bills)
