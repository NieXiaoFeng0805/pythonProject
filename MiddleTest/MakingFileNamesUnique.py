# @Time: 2022/5/26 11:44
# @Author: 丨枫
# @File MakingFileNamesUnique.py
class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        # print(names.count(names[0]))
        # 无重复情况
        countNum = 0

        for i in names:
            if names.count(i) == 1:
                continue
            else:
                countNum += 1
        if countNum == 0:
            return names
        """# 有重复的情况
        addNum = 1
        # 原来没括号后加的再次重复
        addFlag = 0
        for i in range(len(names) - 1, 0, -1):
            needCheck = names.count(names[i])
            # 将重复的字符串进行处理
            for j in range(needCheck):
                needCheck = names.count(names[i])
                if needCheck > 1 and addFlag == 1:  # 原来没括号加上后重复的
                    names[i] = names[i].replace(names[i], names[i][:-3:] + '(' + str(j + 1) + ')')
                    addFlag = 0
                    continue
                if needCheck > 1 and len(names[i]) > 3:  # 有重复的且原来带括号
                    # 将重复的替换掉
                    # print(names[i][:-3:]+'('+str(i)+')')
                    names[i] = names[i] + '(' + str(j + 1) + ')'
                    break
                if needCheck > 1 and names[i].find('(') == -1:  # 有重复不带括号
                    names[i] = names[i] + '(' + str(j + 1) + ')'
                    addFlag = 1  # 将标志置为1
                    continue"""

        """# 重复情况
        # 1、开始不带括号且重复，需要添加括号且添加后没有再次重复
        # 2、开始不带括号且重复，需要添加括号且添加后再次重复
        # 3、开始有括号且重复，再次添加括号后没有再次重复
        # 4、开始有括号且重复，再次添加括号后再次重复

        addNum = 1  # 括号内加的数
        for i in range(len(names) - 1, 0, -1):  # 判断是否重复
            reCount = names.count(names[i])
            if reCount > 1 and names[i].find('(') == -1:  # 有重复且不带括号
                # 加上括号
                names[i] = names[i] + '(' + str(addNum) + ')'
                # 判断加上括号后是否还是重复,重复就重新赋值
                while names[::].count(names[i]) > 1:
                    names[i] = names[i][:-3:] + '(' + str(addNum) + ')'
                    addNum += 1
                addNum = 1
            if reCount > 1 and names[i].find(')') != -1:  # 有重复且带括号
                print("sda")
        print(names)
        return names"""

        namesDic = {}  # 存放每个文件名的数目
        res = []  # 存放结果
        for j in names:
            if j not in namesDic:  # 如果不再字典中，就直接加入结果集中
                res.append(j)
                namesDic[j] = 1  # 设置键值对
                # print(namesDic)
            else:  # 在字典中,表示重复了
                curName = j + "(" + str(namesDic[j]) + ")"
                # print(curName)
                namesDic[j] += 1  # 将对应键的值加1
                while curName in namesDic:  # 判断修改后是否还是重复
                    curName = j + "(" + str(namesDic[j]) + ")"  # 更新后缀名
                    namesDic[j] += 1  # 修改次数加一
                res.append(curName)  # 修改完成存入结果集
                namesDic[curName] = 1  # 设置新的键值对
        # print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    # names = ["onepiece", "onepiece", "onepiece(1)", "onepiece(3)", "onepiece"]
    names = ["kaido", "kaido(1)", "kaido", "kaido(1)"]
    Test.getFolderNames(names)
