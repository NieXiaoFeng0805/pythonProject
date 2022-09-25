# @Time: 2022/9/18 12:13
# @Author: 丨枫
# @File Power of Two.py
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        nums = [i for i in range(33)]
        print(nums)
        for i in nums:
            if 2 ** i == n:
                return True
        return False


if __name__ == '__main__':
    Test = Solution()
    Test.isPowerOfTwo(n=4)
