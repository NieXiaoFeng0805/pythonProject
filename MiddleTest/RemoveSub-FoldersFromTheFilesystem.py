# @Time: 2022/5/26 11:15
# @Author: 丨枫
# @File RemoveSub-FoldersFromTheFilesystem.py
class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        # 暴力解法（超时）
        '''
        # 找子串再把父串删除，留下的就是父文件夹
        # 标记动态下标
        folder = sorted(folder)  # 先排个序
        index = 1
        folderLength = len(folder)
        for i in range(folderLength - 1):
            # 在剩余的元素中查找是否有子串
            while index < folderLength:
                # 遍历到最后一个字符串就跳出
                if i + 1 >= folderLength:
                    break
                # 判断同级目录,是子串但在父串中的字串末尾不是‘/’
                if folder[i + 1].find(folder[i]) != -1 and folder[i + 1][len(folder[i])] != '/':
                    index += 1
                # 判断第i个是否为后面的子串
                if folder[i + 1].find(folder[i]) != -1 and folder[i + 1][len(folder[i])] == '/':  # 第i个是后面的字串
                    # 将第index个移除
                    folder.remove(folder[i + 1])  # 移除后游标不动
                    folderLength = len(folder)  # 更新长度
                else:
                    # 当前字符串不是目标的父串，游标往右移动
                    index += 1
            index = 1
        print(folder)
        return folder'''

        resList = []  # 返回列表
        Format = '//'  # 文件路径格式
        for f in sorted(folder):  # 遍历排序后的列表，保证都是从父文件/同级文件开始
            # 分两种情况
            # 1、结果列表中没有数据时，直接添加第一个字串
            # 2、结果列表中已有数据，判断是否以其进行开头；是的话就是子文件夹，否则是父文件夹或同级目录
            if not f.startswith(Format):
                resList.append(f)
                Format = f + '/'
        return resList


if __name__ == '__main__':
    Test = Solution()
    folder = ["/ah/al/am", "/ah/al"]
    Test.removeSubfolders(folder)
