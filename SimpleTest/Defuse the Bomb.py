# @Time: 2022/9/24 9:24
# @Author: 丨枫
# @File Defuse the Bomb.py
class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        codeList = code * 3
        print(codeList)
        p = 0
        while p < n:
            if k > 0:
                code[p] = sum(codeList[n + p + 1:n + p + k + 1])
            else:
                code[p] = sum(codeList[n + k + p:n + p])
                pass
            p += 1
        print(code, codeList)
        return code


if __name__ == '__main__':
    Test = Solution()
    Test.decrypt(code=[2, 4, 9, 3], k=-2)
