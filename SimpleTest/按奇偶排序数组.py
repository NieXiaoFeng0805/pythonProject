# @Time: 2022/4/28 12:16
# @Author: 丨枫
# @File 按奇偶排序数组.py
class Solution(object):
    def sortArrayByParity(self, nums):
        # 循环遍历，将偶数拿出来放入新数组，同时删除原数组中的偶数
        # 将删除元素后的原数组加在新数组后面即可

        EvenNumber = []
        oddNumber = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                EvenNumber.append(nums[i])
            else:
                oddNumber.append((nums[i]))
        # print(EvenNumber)
        # print(oddNumber)
        #将奇数组排到偶数组后面
        EvenNumber.extend(oddNumber)
        # print(EvenNumber)
        return EvenNumber
        """
        :type nums: List[int]
        :rtype: List[int]
        """


if __name__ == '__main__':
    Test = Solution()
    nums = [3, 1, 2, 4]
    Test.sortArrayByParity(nums)
