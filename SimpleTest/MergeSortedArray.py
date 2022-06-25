# @Time: 2022/5/6 11:18
# @Author: 丨枫
# @File MergeSortedArray.py
import instance as instance


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = 0
        if len(nums1) == 1 and nums1[0] == 0:
            nums1[0] = nums2[0]
        if len(nums1) == 1 and nums1[0] != 0:
            nums1[0] = nums1[0]
        else:
            while i < n:
                nums1.pop(m)
                i += 1
            print(nums1)
            nums1.extend(nums2)
            nums1.sort()
            print(nums1)

        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """


if __name__ == '__main__':
    Test = Solution()
    nums1 = [0, 0, 0, 0, 0]
    m = 0
    nums2 = [1, 2, 3, 4, 5]
    n = 5
    Test.merge(nums1, m, nums2, n)
