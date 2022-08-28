# @Time: 2022/8/23 11:12
# @Author: 丨枫
# @File MirrorFlipAndAdd.py


class Solution:
    def numberOfPairs(self, nums: list[int]) -> int:
        # 将原题中的判断AT + B = BT + A 变为 AT-A = BT-B
        def nums_T(nums):  # 将数组进行镜像翻转并将其与原数组对应数相减
            newNums = [0]*len(nums)  # 存储镜像翻转后相减的数
            nums_dict = {}
            for i in range(len(nums)):
                newNums[i] = int(str(nums[i])[::-1]) - nums[i]
                if newNums[i] not in nums_dict:
                    nums_dict[newNums[i]] = 1
                else:
                    nums_dict[newNums[i]] += 1
            return newNums, nums_dict

        newNums, nums_dict = nums_T(nums)
        print(nums)
        print(newNums)
        print(nums_dict)
        count = 0
        for j in nums_dict:
            if nums_dict[j] >= 2:
                count += sum(i for i in range(nums_dict[j]))
        print(count)
        return count % (10 ** 9 + 7)


if __name__ == '__main__':
    Test = Solution()
    Test.numberOfPairs(nums=[10, 22, 9, 58, 87, 80, 14, 47, 7, 11, 3, 66, 97, 29, 47, 3, 36, 34, 43, 25])
