# @Time: 2022/4/20 13:42
# @Author: 丨枫
# @File 删除有序数组中的重复项.py
class Solution(object):
    def removeDuplicates(self, nums):
        # ums = set(nums)
        # nums = list(nums)
        # print(nums)
        # return len(nums)

        # 原地修改数字
        n = len(nums)
        first = second = 1
        while first < n:
            if nums[first] != nums[first - 1]:
                nums[second] = nums[first]
                second += 1
            first += 1
        print('修改后', second)
        return second


if __name__ == '__main__':
    nums = [1, 1, 2, 3, 4, 5]
    print('修改前', len(nums))
    test = Solution()
    test.removeDuplicates(nums)
