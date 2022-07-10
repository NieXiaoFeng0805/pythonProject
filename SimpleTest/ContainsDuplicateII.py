# @Time: 2022/7/5 12:40
# @Author: 丨枫
# @File ContainsDuplicateII.py
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 用字典记录下标和当前值
        res_dict = {}
        for index, val in enumerate(nums):
            if val in res_dict and index - res_dict[val] <= k:  # 字典中有这个值并且两下标之差小于k
                return True
            res_dict[val] = index  # 否则将新值添加到字典中
        return False


if __name__ == '__main__':
    Test = Solution()
    nums, k = [1, 2, 3, 1], 3
    Test.containsNearbyDuplicate(nums, k)
