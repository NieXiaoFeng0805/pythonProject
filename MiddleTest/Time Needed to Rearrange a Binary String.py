# @Time: 2022/8/28 14:17
# @Author: 丨枫
# @File Time Needed to Rearrange a Binary String.py
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        # 一般做法
        """
        count_1, count_0 = s.count('1'), s.count('0')
        target = '1' * count_1 + '0' * count_0  # 目标字符串
        if s == target:
            return 0
        n = len(s)
        count = 0  # 计数器
        s_list = [i for i in s]
        print(s_list)
        new_s = s
        while new_s != target:
            l, r = 0, 1
            while r < n:
                if s_list[l] == '0' and s_list[r] == '1':
                    s_list[l], s_list[r] = '1', '0'
                    l = r + 1
                    r = l + 1

                else:
                    l += 1
                    r += 1
            count += 1
            new_s = ''.join(s_list)
        print(count)
        return count"""

        # 优化，使用replace进行’01‘的替换
        """
        count = 0  # 计数器
        while '01' in s:
            s = s.replace('01', '10')
            count += 1
        print(count)
        return count"""

        # 再优化
        """
        详细证明：

每个 11 向左移动的过程中，有两种情况：

在到达最终位置之前，未受到左侧的 11 的 “阻挡”，也就是每一秒都移动了一次，此时，移动次数 = 其左侧 00 的个数；
在到达最终位置之前，受到了左侧 11 的 “阻挡”，也就是说，在某一时刻，其与左侧的 11 相邻而组成了 1111。
在此之后，我们可以证明，当左侧的那个 11 到达最终位置时，右侧的 11 一定与左侧的 11 间隔 11 个 00。此时，移动次数 = 左侧 11 的移动次数 + 11。
        """
        res, count = 0, 0
        for i in s:
            if i == '0':
                count += 1
            elif count:
                res = max(res + 1, count)
        print(res)


if __name__ == '__main__':
    Test = Solution()
    Test.secondsToRemoveOccurrences(s="0110101")
