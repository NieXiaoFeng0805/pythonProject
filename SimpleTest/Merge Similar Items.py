# @Time: 2022/8/27 19:59
# @Author: 丨枫
# @File Merge Similar Items.py
class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        """
        item1_dict = {key: value for key, value in items1}
        item2_dict = {key: value for key, value in items2}
        print(item1_dict, item2_dict)
        len1, len2 = len(items1), len(items2)  # 获取遍历最大长度
        theSum = []
        if len1 >= len2:
            for i in item1_dict:
                if i not in item2_dict:  # 不在2号中
                    theSum.append([i, item1_dict[i]])
                else:
                    theSum.append([i, item1_dict[i] + item2_dict[i]])
        else:
            for i in item2_dict:
                if i not in item1_dict:  # 不在1号中
                    theSum.append([i, item2_dict[i]])
                else:
                    theSum.append([i, (item1_dict[i] + item2_dict[i])])

        theSum = sorted(theSum, key=lambda x: x[0])
        print(theSum)
        return theSum"""

        items1.extend(items2)  # 先拼接
        lenarr = len(items1)  # 获取长度
        newarr = sorted(items1, key=lambda x: x[0])  # 排序
        reDict = {}
        for i in range(lenarr):
            if newarr[i][0] in reDict:  # 存在里面
                reDict[newarr[i][0]] += newarr[i][1]
            else:
                reDict[newarr[i][0]] = newarr[i][1]
        print(reDict)
        res = []
        for k, v in reDict.items():
            res.append([k, v])
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    Test.mergeSimilarItems(items1=[[1, 1], [4, 5], [3, 8]], items2=[[3, 1], [1, 5]])
