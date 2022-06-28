# @Time: 2022/6/28 10:10
# @Author: 丨枫
# @File WiggleSortII.py
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 按降序进行排序，再将其从中间拆分
        # 拆分时分奇偶两种情况；奇数序列时，保证较小序列长度大于较大序列，否则会出问题；偶数序列对半分即可
        # 对于大的那一部分，按序将较小的部分间隔插入即可
        nums.sort(reverse=True)
        print(nums)
        minLists, maxLists = [], []
        # 判断奇偶
        n = len(nums)
        if n % 2 == 0:  # 偶
            # 拆分列表
            maxLists.extend(nums[0:n // 2])
            minLists.extend(nums[n // 2:n])
        else:  # 奇数列表，要保证较小列表长度大于较大列表，要不然会出问题
            # 拆分列表
            maxLists.extend(nums[0:n // 2])
            minLists.extend(nums[n // 2:n])
        print(minLists, maxLists)

        # 插入
        i, j = 0, 0
        while i < len(minLists):
            maxLists.insert(j, minLists[i])
            i += 1
            j += 2
        print(maxLists)
        for i in range(n):
            nums[i] = maxLists[i]


if __name__ == '__main__':
    Test = Solution()
    nums = [1, 4, 3, 4, 1, 2, 1, 3, 1, 3, 2, 3, 3]
    Test.wiggleSort(nums)
