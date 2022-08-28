# @Time: 2022/6/26 10:06
# @Author: 丨枫
# @File 3Sum.py
import itertools as its


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 超时
        """if len(nums) < 3:  # 元素小于3个直接返回
            return []
        data = its.combinations(nums, 3)  # 进行组合
        data1 = set(data)  # 去重
        print("data=", list(data))
        print(data1)
        resList = []
        for i in data1:
            if sum(i) == 0:  # 元素和为0则将i排序后去重再添加到结果列表中
                i = sorted(i)
                if i in resList:
                    continue
                else:
                    resList.append(i)
        print(resList)
        return resList"""

        # 优化
        n = len(nums)
        if not nums or n < 3:  # 小于三个元素直接返回
            return []
        nums.sort()  # 进行排序
        res = []
        for i in range(n):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 从两端往中间遍历
            L = i + 1
            R = n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:  # 三者相加刚好等于0
                    res.append([nums[i], nums[L], nums[R]])
                    # 防止重复
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R = R - 1

                    L = L + 1
                    R = R - 1
                elif nums[i] + nums[L] + nums[R] > 0:  # 相加大于0，右边大了，右指针往左移动
                    R = R - 1
                else:  # 相加小于0，左指针往右移动
                    L = L + 1
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    Test.threeSum(nums)
