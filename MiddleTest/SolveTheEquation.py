# @Time: 2022/8/11 16:46
# @Author: 丨枫
# @File SolveTheEquation.py
import re


class Solution:
    def solveEquation(self, equation: str) -> str:
        """
        index_equal = equation.index('=')
        part1 = equation[0:index_equal]  # 第一部分
        part2 = equation[index_equal + 1:]  # 第二部分
        print(part1, part2)

        count_x = 0  # 计算x个数
        num_list = []  # 存放数
        num_sum = 0  # 数的和
        part1_list = re.findall(r'[+-]?\d+|[+-]?\D', part1)
        part2_list = re.findall(r'[+-]?\d+|[+-]?\D', part2)
        print(part1_list, part2_list)
        for i in part1_list:
            if i == 'x' or i == '+x':
                count_x += 1
            elif i == '-x':
                count_x -= 1
            else:
                num_sum += int(i)
        # print(count_x, num_sum)
        num_sum = -num_sum
        for i in part2_list:
            if i == 'x' or i == '+x':
                count_x -= 1
            elif i == '-x':
                count_x += 1
            else:
                num_sum += int(i)
        # print(count_x, num_sum)
        if count_x == 0:
            return 'x=0'
        res = num_sum//count_x
        return 'x='+str(res)"""
        # 化为 kx = b 的形式
        left, k, b, neg = 1, 0, 0, 1
        cur = ""
        for e in equation:
            if e == 'x':  # 若是单独x出现
                num = int(cur) if cur else 1
                k += left * neg * num  # 计算系数
                cur = ""
            elif e in "+-=":  # 若出现标点
                if cur:
                    num = int(cur)
                    b += -left * neg * num
                if e == '=':
                    left = -1
                    neg = 1
                elif e == '-':
                    neg = -1
                else:
                    neg = 1
                cur = ""
            else:
                cur += e
        if cur:
            b += -left * neg * int(cur)
        if k == 0:
            return "Infinite solutions" if b == 0 else "No solution"
        return f"x={b // k}"


if __name__ == '__main__':
    Test = Solution()
    Test.solveEquation(equation="x=x")
