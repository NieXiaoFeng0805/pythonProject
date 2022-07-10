# @Time: 2022/7/6 15:49
# @Author: 丨枫
# @File MaxConsecutiveOnesIII.py
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 原版
        """        
        if k == 0:
            return (len(nums) - 1) - nums.count(0)

        # 设置两个指针表示窗口左右边界
        # 窗口的增大知道翻转的1用完
        left, right = 0, 0
        maxOne = 0  # 包含1的最大值
        nums_copy = nums.copy()
        k_copy = k
        while right < len(nums) - 1:
            if nums[right] == 0:  # 遇见0进行翻转
                nums_copy[right] = 1
                k_copy -= 1  # 可翻转数减一
            right += 1  # 右边界移动
            if k_copy == 0:  # 翻转次数用完,获取包含1最大数
                if nums[right] == 1:
                    continue    
                maxOne = max(maxOne, (right - left+1))
            # 判断左边界是否需要移动
            while k_copy == 0 and right < len(nums) - 1:
                left += 1
                k_copy = k
                right = left

        print(maxOne)
        return maxOne"""

        # 优化
        # 将问题转为最大子数组中最多含有k个0即可
        left, right = 0, 0  # 设置窗口左右边界
        max_length = 0
        count_0 = 0
        while right < len(nums):
            if nums[right] == 0:
                count_0 += 1
            while count_0 > k:  # 0的个数超出k值
                if nums[left] == 0:  # 窗口左边界为0则将0的个数减1；因为等下要移动左边界
                    count_0 -= 1
                left += 1
            max_length = max(max_length, right - left + 1)  # 更新最大值
            right += 1
        print(max_length)
        return max_length


if __name__ == '__main__':
    Test = Solution()
    nums, k = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2
    Test.longestOnes(nums, k)
