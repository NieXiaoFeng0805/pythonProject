# @Time: 2022/8/30 14:11
# @Author: 丨枫
# @File Make Array Zero by Subtracting Equal Amounts.py
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        # 常规做法
        """
        count_0, res = nums.count(0), 0  # 记录0的个数和全变为0的次数
        n = len(nums)
        nums.sort()  # 排序
        while count_0 != n:
            sub = nums[count_0]  # 除0外最小值
            for i in range(count_0, n):
                nums[i] -= sub
                if nums[i] == 0:
                    count_0 += 1
            res += 1
        print(res)
        return res"""
        # 变成集合
        # 因为需要计算变成0的次数，所以将非零不重复数全部变为0 的步数即为其长度
        newNums = set(nums) - {0}
        return len(newNums)


if __name__ == '__main__':
    Test = Solution()
    Test.minimumOperations(nums=[1, 5, 0, 3, 0])
