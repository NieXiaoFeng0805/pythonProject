# @Time: 2022/9/25 13:17
# @Author: 丨枫
# @File Rotated Digits.py
class Solution:
    def rotatedDigits(self, n: int) -> int:
        goodNum = ['2', '5', '6', '9']
        badnum = ['3', '4', '7']
        res = 0

        for i in range(1, n + 1):
            flag = False
            str_n = str(i)
            n_list = [i for i in str_n]
            # if n_list.count(n_list[0]) == len(n_list) and len(n_list) > 1:  # 翻转后值不变
            #     continue
            for j in n_list:
                if j in badnum:
                    flag = False
                    break
                elif j in goodNum:
                    flag = True
            if flag:
                res += 1
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    Test.rotatedDigits(n=857)
    # Test.rotatedDigits(n=28)
