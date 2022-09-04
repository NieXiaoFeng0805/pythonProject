# @Time: 2022/8/30 14:46
# @Author: 丨枫
# @File Maximum Number of Groups Entering a Competition.py
class Solution:
    def maximumGroups(self, grades: list[int]) -> int:
        res = 1  # 计算组数，默认为1
        p = 1  # 初始人数
        add = 2  # 增加人数
        n = len(grades)
        while p < n:
            p += add
            if p > n:
                break
            res += 1
            add += 1

        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    Test.maximumGroups(grades=[10, 6, 12, 7, 3, 5])
