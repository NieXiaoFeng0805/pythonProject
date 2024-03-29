# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/2/28 11:20
# software: PyCharm
"""
文件说明：

"""


class Solution:
    def maxArrayValue(self, nums) -> int:
        s = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            s = s + nums[i] if nums[i] <= s else nums[i]
        return s



Solution().maxArrayValue(nums=[2, 3, 7, 9, 3])
Solution().maxArrayValue(nums=[5, 3, 3])
