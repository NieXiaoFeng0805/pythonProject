# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/28 16:48
# software: PyCharm
"""
文件说明：

"""


class Solution:
    # 超时
    def firstDayBeenInAllRooms(self, nextVisit) -> int:
        '''
        1997
        字典存储房间号：改房间的访问次数
        设置一个集合存放已经访问过的房间，当集合长度 == n 时，结束循环
        :param nextVisit:
        :return:
        '''
        home_index = set()
        visit = 0  # 初始访问房间下标
        cnt = 0  # 记录天数
        n = len(nextVisit)
        home_dict = dict(zip([i for i in range(n)], [0 for _ in range(n)]))  # 下标以及访问次数
        while len(home_index) < n:
            home_dict[visit] += 1  # 当前房间的访问次数+1
            if home_dict[visit] % 2 != 0:  # 奇数
                visit = nextVisit[visit]  # 更换房间
            else:  # 偶数
                visit = (visit + 1) % n
            home_index.add(visit)  # 添加访问过的房间号
            cnt += 1  # 天数+1
        return cnt

    # 优化
    def new_firstDayBeenInAllRooms(self, nextVisit):
        s = [0] * len(nextVisit)
        for i, j in enumerate(nextVisit[:-1]):
            s[i + 1] = (s[i] * 2 - s[j] + 2) % (10 ** 9 + 7)
        return s[-1]


# Solution().firstDayBeenInAllRooms(nextVisit=[0, 0])
Solution().firstDayBeenInAllRooms(
    nextVisit=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0])
