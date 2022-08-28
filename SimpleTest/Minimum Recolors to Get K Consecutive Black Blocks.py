# @Time: 2022/8/28 13:24
# @Author: 丨枫
# @File Minimum Recolors to Get K Consecutive Black Blocks.py


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # 若不用 转变就满足条件则返回0
        new_block = blocks.split('W')
        if len(max(new_block)) >= k:
            return 0
        if len(blocks) == k:
            return blocks.count('W')

        left, right = 0, k  # 两个指针标识窗口的开端和末端
        n = len(blocks)
        res = 100
        while right <= n:
            temp = blocks[left:right]  # 指定窗口的长度
            # 判断这个窗口中w的个数，将最小w的个数返回
            res = min(res, temp.count('W'))
            left += 1
            right += 1
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    Test.minimumRecolors(blocks="WBBWWBBWBW", k=7)
