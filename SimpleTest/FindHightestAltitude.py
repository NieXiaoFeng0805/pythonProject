# @Time: 2022/4/25 10:49
# @Author: 丨枫
# @File FindHightestAltitude.py

# Topic Describes:有一个自行车手打算进行一场公路骑行，这条路线总共由n + 1个不同海拔的点组成。自行车手从海拔为 0的点0开始骑行。
#
# 给你一个长度为 n的整数数组gain，其中 gain[i]是点 i和点 i + 1的 净海拔高度差（0 <= i < n）。请你返回 最高点的海拔 。


class Solution(object):
    def largestAltitude(self, gain):
        # 净海拔高度差 第i+1个点减去第i个点
        # 海拔高度数组
        startArr = [0]  # 第一个元素为0
        for i in range(len(gain) + 1):
            if i == 0:
                continue
            altitude = gain[i - 1] + startArr[i - 1]
            startArr.append(altitude)
        # print(startArr)
        # 找最大值
        startArr.sort(reverse=True)
        # print(startArr[0])
        return startArr[0]


if __name__ == '__main__':
    gain = [-5, 1, 5, 0, -7]
    Test = Solution()
    Test.largestAltitude(gain)
