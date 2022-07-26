# @Time: 2022/7/23 15:32
# @Author: 丨枫
# @File RebuildingSequence.py
from collections import defaultdict
from itertools import pairwise


class Solution:
    def sequenceReconstruction(self, nums: list[int], sequences: list[list[int]]) -> bool:
        d = defaultdict(set)  # 构建默认字典防止键不在字典中时报错(若键不在字典中则返回一个默认值)
        for seq in sequences:  # 遍历序列
            for i in range(1, len(seq)):  # 对每个序列的元素进行遍历并将其加入到字典中
                d[seq[i - 1]].add(seq[i])
        for a, b in pairwise(nums):  # 返回从nums中连续的重叠对，即1，2；2，3
            if b not in d[a]:  # 出现没有按顺序来的序列，说明可以有它的翻转同样能实现nms，则其不是超序列
                return False
        return True


if __name__ == '__main__':
    Test = Solution()
    nums, sequences = [1, 2, 3], [[1, 2], [1, 3]]
    Test.sequenceReconstruction(nums, sequences)
