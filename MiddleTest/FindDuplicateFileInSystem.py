# @Time: 2022/6/1 10:56
# @Author: 丨枫
# @File FindDuplicateFileInSystem.py
import re


class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        """
        1、将每个文件的完整路径拼出存入列表中转入2
        2、对完整路径进行遍历，用正则表达式将文件内容取出作为键，路径作为值进行匹配。进入3或4
        3、对于未重复的内容，将其值作为空列表，随后添加新路径
        4、对于重复内容，将其添加到对于键所在的列表中
        5、以字典的键遍历字典，将键所对应的值列表且长度大于1的添加到返回列表中，最后返回即可   
        """
        savePath = []  # 存储路径
        PathDict = {}  # 存储散列表
        for path in paths:
            tempList = path.split(' ')  # 将每个元素的文件路径存储起来
            # print(tempList)
            for i in range(len(tempList) - 1):  # 并凑路径
                thePath = tempList[0] + '/' + tempList[i + 1]
                # print(thePath)
                savePath.append(thePath)  # 每个文件的路径
        print(savePath)
        for i in range(len(savePath)):
            findall = re.findall(r'[(](.*?)[)]', savePath[i])  # 取出括号内的值
            # print(findall)
            # 将匹配到的内容作为键
            if findall[0] not in PathDict:  # 出现新的内容则作为新的键
                PathDict[str(findall[0])] = []
                # 添加新值并将内容部分去除
                PathDict[str(findall[0])].append(savePath[i][:(savePath[i].index('(')):])
            else:  # 文件内容重复，将其添加到对应键的列表中
                PathDict[str(findall[0])].append(savePath[i][:(savePath[i].index('(')):])
        print(PathDict)
        resList = []
        # 遍历字典，将结果列表返回
        for key in PathDict.keys():
            # print(len(PathDict.get(key)))
            # 将长度大于2的添加到返回列表中
            if len(PathDict.get(key)) >= 2:
                resList.append(PathDict.get(key))
        print(resList)
        return resList


if __name__ == '__main__':
    Test = Solution()
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
    Test.findDuplicate(paths)
