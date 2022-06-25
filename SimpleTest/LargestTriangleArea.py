# @Time: 2022/5/15 10:45
# @Author: 丨枫
# @File LargestTriangleArea.py
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # 线性代数——行列式计算面积
        # 最大面积 S = 0.5 * abs(ad+cf+be-af-de-bc)
        MaxArea = 0
        for i in points:
            for j in points:
                for k in points:
                    MaxArea = max(MaxArea, abs(i[0]*j[1] + j[0]*k[1] + i[1]*k[0] - i[0]*k[1] - j[1]*k[0] - i[1]*j[0]))
        print(MaxArea * 0.5)
        return MaxArea * 0.5
if __name__ == '__main__':
    Test = Solution()
    points = [[1,0],[0,0],[0,1]]
    Test.largestTriangleArea(points)