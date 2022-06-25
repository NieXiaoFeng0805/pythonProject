# @Time: 2022/5/31 10:03
# @Author: 丨枫
# @File LongestAbsoluteFilePath.py
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # 先判断有没有文件
        # 有文件则需找到其上级目录，将其存入文件路径中
        """
        :param input:
        :return: int:
        """
        """
        1、以‘/n’拆分字符串，表示各级文件
        2、计算‘/t’的个数，数目最大的代表路径最长
            若存在文件深度即‘/t’数目相同，则比较整条路径的长度
        3、找到最深文件并以’/‘为连接符进行路径的拼凑，最后返回路径长度
        """

        """if '.' not in input:  # 字符串中没有后缀名则返回0
            return 0
            # print(input)
        s = input.split('\n')
        print('s=', input.split('\n'))
        count_T = []  # 由'\'的个数组成，其下标对应着文件路径的下标
        for i in s:
            count_T.append(i.count('\t'))
        # print(count_T)
        # print(count_T.index(max(count_T)))
        maxCount_T_index = count_T.index(max(count_T))  # 深度最大的文件所在下标
        j = 0
        FilePath = []
        if maxCount_T_index == 0:  # 都在根目录下
            # print(len('/'.join(s)))
            # 全部在根目录下
            for v in s:
                if '.' not in v:  # 路径中带有根目录需要拼路径
                    flag = True
                    break
                else:
                    flag = False
            if flag:
                for path in range(len(s)):  # 将空格删除
                    s[path] = s[path].replace(" ", "")
                print(len('/'.join(s)))
                return len('/'.join(s))
            else:
                return len(max(s))

        while j < count_T[maxCount_T_index]:  # 将路径组合
            s[maxCount_T_index - j] = s[maxCount_T_index - j].replace('\t', '')  # 将‘\t’去掉
            FilePath.append(s[maxCount_T_index - j])  # 组合路径
            j += 1
        FilePath.reverse()  # 原地翻转
        Max_path = s[0] + '/' + '/'.join(FilePath)
        # print(Max_path)
        # print(len(Max_path))
        return len(Max_path)"""

        res = 0
        depth_length_map = {-1: 0}
        s = input.split('\n')
        for line in s:
            depth = line.count('\t')  # 表示有多少层
            print('depth=', depth)
            # 每行 \t 空格最后要被去掉
            depth_length_map[depth] = depth_length_map[depth - 1] + len(line) - depth
            if line.count('.'):  # 已经到文件了，即到底了
                # 每层都要添加depth个 /
                res = max(res, depth_length_map[depth] + depth)
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    input = "dir\n        file.txt"
    # input = "file1.txt\nfile2.txt\nlongfile.txt"
    Test.lengthLongestPath(input)
