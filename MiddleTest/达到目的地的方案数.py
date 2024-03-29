# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/5 9:15
# software: PyCharm
"""
文件说明： Dijksstra算法

"""


# 定义n[i][j] 表节点i->j这条边的边权。若不存在则设为♾️
# 定义dis[i]表节点 0->i的最短路径  （初始态dis[0]=0，dis[i]=∞）
# 计算出dis数组
#   首先更新节点0到邻居y的最短路径  更新 dis[y] 为 n[0][y]
#   然后取除节点0外的dis[i]的最小值，即dis[i]已经是节点 0 到 i 的最短路径
#   用节点i到其 邻居 y的边权g[i][y]更新dis[y]
#       若dis[i]+g[i][y] <dis[y]; 则更新dis[y] 为 dis[i]+g[i][y]；否则不更新
#   然后取出了节点 0，i 外的dis[i] 的最新小值，重复上面步骤
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        g = [[inf for _ in range(n)] for _ in range(n)]  # 邻接矩阵
        for x, y, d in roads:  # 为每对节点间赋边权
            g[x][y] = d
            g[y][x] = d

        dis = [inf] * n  # 结果数组，初始都为♾️
        dis[0] = 0  # 节点0到自身的距离
        f = [0] * n  # 表示节点0到节点i的最短路的个数
        f[0] = 1
        done = [False] * n

        while True:
            x = -1
            for i, ok in enumerate(done):
                if not ok and (x < 0 or dis[i] < dis[x]):
                    x = i
            if x == n - 1:  # 到末节点了
                return f[-1]
            done[x] = True  # 最短路长度已确定（无法变得更小）
            dx = dis[x]

            # 更新x的邻居的最短路
            for y, d in enumerate(g[x]):
                new_dis = dx + d
                if new_dis < dis[y]:
                    # 最短路径必然经过x
                    dis[y] = new_dis
                    f[y] = f[x]
                elif new_dis == dis[y]:  # 和最短一样长
                    f[y] = (f[y] + f[x]) % (10 ** 9 + 7)
