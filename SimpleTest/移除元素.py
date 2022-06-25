# @Time: 2022/4/20 14:04
# @Author: 丨枫
# @File 移除元素.py
import length as length


class Solution(object):
    def removeElement(self, nums, val):
        # for i, v in enumerate(nums):
        #     if v == val:
        #         nums.remove(v)
        #         # 删除后长度会变！此方法不行
        i = 0
        while i < len(nums):
            if val == nums[i]:
                nums.remove(nums[i])
                if nums == []:
                    return len(nums)
                if i == 0:
                    continue
                i -= 1
                continue
            i += 1
        print('修改后', nums)
        return len(nums)


if __name__ == '__main__':
    test = Solution()
    nums = [2, 2, 2, 1]
    print('修改前', nums)
    test.removeElement(nums, 2)
