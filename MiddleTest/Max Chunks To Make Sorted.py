# author: Feng
# contact: 1245272985@qq.com
# datetime:2022/10/13 10:42
# software: PyCharm
"""
文件说明：

"""


class Solution:
    def maxChunksToSorted(self, arr: list) -> int:
        n = len(arr)
        res = [[] for i in range(n)]  # 结果数组
        # res[0][0] = arr[0]
        print(res)
        for i in range(1, n):
            if arr[i] < arr[i - 1]:  # 出现逆序，加入到一个组中
                res[i - 1].append(arr[i])
                continue
            else:  # 升序，每个元素作为一组
                res[i].append(arr[i])
                continue
        print(res)
        return len(res)


if __name__ == '__main__':
    Test = Solution()
    Test.maxChunksToSorted(arr=[4, 3, 2, 1, 0])
