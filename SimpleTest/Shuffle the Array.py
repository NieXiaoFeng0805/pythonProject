# @Time: 2022/8/29 13:29
# @Author: 丨枫
# @File Shuffle the Array.py
class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    Test.shuffle(nums=[2, 5, 1, 3, 4, 7], n=3)
