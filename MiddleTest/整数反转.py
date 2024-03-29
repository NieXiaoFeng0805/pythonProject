# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/4 20:49
# software: PyCharm
"""
文件说明：

"""


class Solution:
    def reverse(self, x: int) -> int:
        strx = str(x)
        n = len(strx)
        x_re = str(x)[::-1]
        if strx[0] == '-':
            x_re = '-' + x_re[:n - 1:]
        res = int(x_re)

        return 0 if res < (-2**31) or res > (2**31-1) else res


if __name__ == '__main__':
    S = Solution()
    S.reverse(x=-123)
