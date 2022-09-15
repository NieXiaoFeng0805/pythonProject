# @Time: 2022/9/9 20:48
# @Author: 丨枫
# @File Crawler Log Folder.py
class Solution:
    def minOperations(self, logs: list[str]) -> int:
        foldList = []
        for i in logs:
            if i == '../':
                if len(foldList) == 0:
                    continue
                foldList.pop()
            elif i == './':
                continue
            else:
                foldList.append(i)
        print(foldList)
        return len(foldList)


if __name__ == '__main__':
    Test = Solution()
    Test.minOperations(logs=["d1/", "../", "../", "../"])
