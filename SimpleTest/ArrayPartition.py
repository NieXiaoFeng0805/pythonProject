# @Time: 2022/8/1 12:32
# @Author: 丨枫
# @File ArrayPartition.py
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()  # 排序
        res = 0  # 返回值
        # print(nums)

        # 既然要将n对中最小的数加起来成相对较大数，则进行排序后两两一组将每组较小元素相加即可
        for i in range(1, len(nums), 2):
            temp1, temp2 = nums[i - 1], nums[i]
            res += min(temp1, temp2)
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    nums = [1, 4, 3, 2]
    Test.arrayPairSum(nums)
