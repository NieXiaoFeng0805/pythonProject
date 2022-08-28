# @Time: 2022/8/24 10:55
# @Author: 丨枫
# @File Make Two Arrays Equal by Reversing Sub-arrays.py
class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        # 遍历做法
        """
        for i in target:
            if i not in arr:
                return False
            else:
                arr.remove(i)
        return True if len(arr) == 0 else False"""

        # 两次排序
        # arr.sort()
        # target.sort()
        # return True if arr == target else False
        print(sorted(arr) == sorted(target))
        return True if sorted(arr) == sorted(target) else False


if __name__ == '__main__':
    Test = Solution()
    Test.canBeEqual(target=[1, 2, 3, 8], arr=[2, 4, 1, 3])
