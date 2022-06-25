# @Time: 2022/6/7 16:40
# @Author: 丨枫
# @File UniquePaths.py
import itertools as iter_t


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """
        1、考虑机器人到终点的情况，无论是哪条路径，向右的次数是n-1次；向下的次数是m-1次;一共是m+n-2次
        2、记向右为R，向下为D；
        3、机器人到达终点的方法等价于将较小的移动在较大的移动次数中插入的种类且不能重复
        4、也即从m+n-2次的移动中选取m-1次向下的移动即可
        """
        # # 如果只有一行或一列，则只有一种情况
        # if min(m, n) == 1:
        #     return 1
        # MoveList = []
        # for i in range(m + n - 2):  # 移动的步数
        #     MoveList.append('M' + str(i))  # 建立移动列表
        # res = list(iter_t.combinations(MoveList, m - 1))  # 用自带的库进行排列组合
        # print(len(res))
        # return len(res)

        # 动态规划实现
        # 如果只有一行或一列，则只有一种情况
        if min(m, n) == 1:
            return 1
        dp = [[0] * n for _ in range(m)]  # 获得m行n列的0矩阵
        # print(dp)
        # 机器人都要先走一步，所以上边界和左边界初始值都设为1
        for i in range(1, n):  # 上边界初值
            dp[0][i] = 1
        for i in range(1, m):  # 左边界赋值
            dp[i][0] = 1
        # 开始规划
        for i in range(1, m):  # 行
            for j in range(1, n):  # 列
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  # 该元素的上一元素+该元素的左边元素
            print(dp[i][j])
        print(dp[-1][-1])
        return dp[-1][-1]


if __name__ == '__main__':
    Test = Solution()
    m, n = 5, 5
    Test.uniquePaths(m, n)
