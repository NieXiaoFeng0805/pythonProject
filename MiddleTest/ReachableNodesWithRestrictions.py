# @Time: 2022/8/12 10:59
# @Author: 丨枫
# @File ReachableNodesWithRestrictions.py
from itertools import chain


class Solution:
    def reachableNodes(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        """valid_edges = []
        for i in edges:
            if i[0] in restricted or i[1] in restricted:  # 包含在被限边内
                continue
            else:
                valid_edges.append(i)
        print(valid_edges)
        # newarr = set(list(chain.from_iterable(valid_edges)))
        # print(newarr)
        count = 1  # 记录有效数
        start = 0  # 起始位
        while True:
            flag = True
            for i in valid_edges:
                if start in i:
                    flag = False
                    start = i[0] if i[0] != start else i[1]  # 下一个数
                    count += 1
                    valid_edges.remove(i)  # 取出
                    break
            if flag:
                print(count)
                break"""
        # DFS方法
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        print(g)
        ans = 0

        def dfs(x: int, fa: int):
            nonlocal ans
            ans += 1
            for y in g[x]:
                if y != fa and y not in restricted:
                    dfs(y, x)

        dfs(0, -1)
        print(ans)


if __name__ == '__main__':
    Test = Solution()
    Test.reachableNodes(n=7, edges=[[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], restricted=[4, 5])
