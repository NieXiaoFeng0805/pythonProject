# @Time: 2022/7/1 12:02
# @Author: 丨枫
# @File DifferentWaysToAddParentheses.py
class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        # 采用分治的算法求解
        # 拆分算式并按要求重新组合运算顺序可知，其组合结果取决与运算数间的结果的组合数；总问题是 x op y能有多少种组合
        # 所以这个问题的子问题是 x op y 中 的运算数其以运算符分隔的左右两侧算式解
        # 分治思想
        # 1、分解：按运算符分为左右两部分，分别求解
        # 2、解决：实现一个递归函数，输入算式，返回算式解
        # 3、合并：根据运算符合并左右两部分的解，得出答案

        # 没有运算符
        if expression.isdigit():
            return [int(expression)]

        res = []  # 结果列表
        for index, val in enumerate(expression):
            if val in ['+', '-', '*']:
                # 1、分解：遇到运算符则计算其两侧的结果集
                # 2、解决：递归求出子问题的解
                left = self.diffWaysToCompute(expression[:index])  # 运算符左边的数
                right = self.diffWaysToCompute(expression[(index + 1):])  # 运算符右边的数
                # 3、合并：根据运算符合并子问题的解
                for l in left:
                    for r in right:
                        if val == '+':
                            res.append(l + r)
                        elif val == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    expression = "2*3-4*5"
    Test.diffWaysToCompute(expression)
