# @Time: 2022/8/7 11:26
# @Author: 丨枫
# @File QueryKthSmallestTrimmedNumber.py
class Solution:
    def smallestTrimmedNumbers(self, nums: list[str], queries: list[list[int]]) -> list[int]:
        res = []  # 返回数组
        for i in queries:  # 遍历要求数组
            k_min, remain = i[0], i[1]
            temp = []  # 记录每次遍历的剩余数组
            for j in nums:
                # print(j[-remain:])
                temp.append(int(j[-remain:]))  # 截取的剩余数位
            # 对截取的数位进行排序
            temp_sort = sorted(temp)
            # 获取对应的最小数
            MinNum = temp_sort[k_min - 1]
            # 判断最小值是否唯一
            if temp.count(MinNum) == 1:
                # 找到对应最小数在为排序前的下标(从后往前查)
                res.append(temp.index(MinNum))
            else:
                if k_min == temp_sort.index(MinNum) + 1:  # 最小值第一个出现的位置
                    res.append(temp.index(MinNum))
                else:  # 出现重复最小值
                    p = k_min - temp_sort.index(MinNum)  # 记录是第几个重复最小值
                    for v in range(len(temp)):  # 遍历，直到遇到要求的小值再添加到返回数组中
                        if temp[v] == MinNum:
                            p -= 1
                        if p == 0:
                            res.append(v)
                            break
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    nums = ["64333639502", "65953866768", "17845691654", "87148775908", "58954177897", "70439926174", "48059986638",
            "47548857440", "18418180516", "06364956881", "01866627626", "36824890579", "14672385151", "71207752868"]

    queries = [[13, 1], [13, 1]]
    Test.smallestTrimmedNumbers(nums, queries)
