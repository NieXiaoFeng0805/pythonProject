# @Time: 2022/8/12 10:20
# @Author: 丨枫
# @File GroupthePeopleGiventheGroupSizeTheyBelongTo.py
class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        gS = set(groupSizes)  # 几种类型
        print(gS)
        res = []  # 返回数组
        # 遍历
        for i in gS:
            temp = []  # 临时存储元素
            while True:
                ele_index = groupSizes.index(i)  # 找到索引
                temp.append(ele_index)  # 添加到临时列表中
                groupSizes[ele_index] = 0  # 替换不会出现的数
                if len(temp) == i:
                    res.append(temp)
                    temp = []
                if i not in groupSizes:  # 这个数遍历完了
                    break
        print(res)


if __name__ == '__main__':
    Test = Solution()
    Test.groupThePeople(groupSizes=[2, 1, 3, 3, 3, 2])
