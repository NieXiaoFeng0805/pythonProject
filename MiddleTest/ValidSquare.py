# @Time: 2022/8/2 14:54
# @Author: 丨枫
# @File ValidSquare.py
class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        res = set()
        side_set = [(p1, p2), (p1, p3), (p1, p4), (p2, p3), (p2, p4), (p3, p4)]
        for i in side_set:  # 遍历集合，正方形的顶点间的距离只有两种情况
            d = ((i[0][0] - i[1][0]) ** 2) + ((i[0][1] - i[1][1]) ** 2)
            res.add(d)
        return True if len(res) == 2 and 0 not in res else False


if __name__ == '__main__':
    Test = Solution()
    p1, p2, p3, p4 = [0, 0], [1, 1], [1, 0], [0, 1]
    Test.validSquare(p1, p2, p3, p4)
