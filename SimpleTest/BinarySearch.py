# @Time: 2022/6/13 10:30
# @Author: 丨枫
# @File BinarySearch.py
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 实现二分查找，要求数据经过排序，确定三个变量存储左、中、右位置
        # 与中间对比，若有则返回游标，小于则在左边，大于在右边
        # 当左标大于右标时未找到则没有
        L, R = 0, len(nums) - 1
        # print(L,R,M)
        while L <= R:
            M = (L + R) // 2
            if nums[M] == target:
                print(M)
                return M
            elif nums[M] > target:  # 中间值大于目标值，在左侧
                R = M - 1  # 将右标改中间-1
            else:  # 在中间值右侧
                L = M + 1  # 将左标改为中标+1
        return -1

if __name__ == '__main__':
    Test = Solution()
    nums, target = [-1, 0, 3, 5, 9, 12], 9
    Test.search(nums, target)
