# @Time: 2022/5/6 10:05
# @Author: 丨枫
# @File PlusOne.py
class Solution(object):
    def plusOne(self, digits):
        # 特殊情况
        if len(digits) == 1 and digits[0] == 9:
            new_digits = []
            new_digits.append(1)
            new_digits.append(0)
            print(new_digits)
            return new_digits
        flag = 1
        for i in digits:
            if i != 9:
                flag = 0
        if flag == 1:
            new_digits1 = []
            new_digits1.append(1)
            for j in range(len(digits)):
                new_digits1.append(0)
            print(new_digits1)
            return new_digits1

        # 一般情况
        else:
            for k in range(len(digits)-1, -1,-1):
                if digits[k]==9:
                    digits[k] = 0
                else:
                    digits[k] += 1
                    break
            print(digits)
            return digits


if __name__ == '__main__':
    Test = Solution()
    digits = [8,9,9]
    Test.plusOne(digits)
