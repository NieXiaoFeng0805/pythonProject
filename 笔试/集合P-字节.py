# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/15 9:20
# software: PyCharm
"""
文件说明：

"""


# 二维平面 整数点集，满足 P中点X，X的右上方区域无点 找到符合条件的X

class Solution:
    def findP(self):
        n, plist = self.create_p()
        plist = sorted(plist)
        print(plist)
        max_y = 0  # 记录最大y值
        res = []
        for i in range(n - 1, -1, -1):
            if not res:
                res.append(plist[i])
            elif plist[i][1] > max_y:
                res.append(plist[i])
            max_y = plist[i][1]  # 更新y值
        for l in range(len(res) - 1, -1, -1):
            print(str(res[l][0]) + ' ' + str(res[l][1]))

    def create_p(self):
        n = int(input())
        p_list = []
        for i in range(n):
            x, y = input().split(' ')
            p_list.append([int(x), int(y)])
        return n, p_list


Solution().findP()
