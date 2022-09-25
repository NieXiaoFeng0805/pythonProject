# @Time: 2022/9/16 14:18
# @Author: 丨枫
# @File Summary Ranges.py
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res = []
        l, r = 0, 1
        n = len(nums)
        if n == 1:
            return [str(nums[0])]
        while r < n:
            temp = 1
            while r < n and nums[l] + temp == nums[r]:
                r += 1
                temp += 1
            if r - l == 1:
                res.append(str(nums[l]))
            else:
                res.append(str(nums[l]) + '->' + str(nums[r - 1]))
            l = r
            if l == n-1:
                res.append(str(nums[l]))
            r += 1
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    Test.summaryRanges(nums= [0,2,3,4,6,8,9])
