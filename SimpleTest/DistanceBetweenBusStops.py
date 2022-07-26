# @Time: 2022/7/24 10:33
# @Author: 丨枫
# @File DistanceBetweenBusStops.py
class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        """
        d_cw = 0  # 顺时针距离
        d_ccw = 0  # 逆时针距离
        if destination - start < 0:  # 小于0 就换一下，反正距离是不会变的
            temp = start
            start = destination
            destination = temp
        # 计算顺时针与逆时针到destination的距离
        d_cw += sum(distance[start:destination])  # 顺时针
        # print(d_cw)
        # 逆时针
        d_ccw += sum(distance[0:start])
        # print(d_ccw)
        counter = start
        for j in range(len(distance) - 1, -1, -1):  # 逆时针
            d_ccw += distance[j]
            counter += 1
            if counter == len(distance) - (destination - start):
                break
        print(d_cw, d_ccw)
        return min(d_cw, d_ccw)
"""
        # 优化
        d_sum, counter, start, destination = 0, 0, min(start, destination), max(start, destination)
        for i, d in enumerate(distance):
            d_sum += d  # 将路径距离全部相加
            if start <= i < destination:  # 当站点值大于等于起始位且小于终点站时，是顺时针距离
                counter += d
        # 最后返回 顺时针距离和逆时针距离(逆时针距离相当于全部距离减去顺时针的距离)较小值
        return min(counter, d_sum - counter)


if __name__ == '__main__':
    Test = Solution()
    distance, start, destination = [7, 10, 1, 12, 11, 14, 5, 0], 7, 2
    # distance, start, destination = [1, 2, 3, 4], 0, 2
    Test.distanceBetweenBusStops(distance, start, destination)
