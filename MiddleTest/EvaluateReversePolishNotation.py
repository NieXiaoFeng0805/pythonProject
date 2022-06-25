# @Time: 2022/5/30 9:36
# @Author: 丨枫
# @File EvaluateReversePolishNotation.py


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        TokenTable = "+-*/"  # 运算符
        res = []  # 结果栈
        for i in range(len(tokens)):
            # 如果在数字集中就入栈
            if tokens[i] not in TokenTable:
                res.append(tokens[i])
            # 如果是运算符就将前两个取出
            else:
                # 计算
                Exp = str(res[len(res) - 2]) + tokens[i] + str(res[len(res) - 1])
                Expres = int(eval(Exp))
                # 将运算数剔除
                res.pop(len(res) - 1)
                res.pop(len(res) - 1)
                # 将结果入栈
                res.append(Expres)
        print(int(res[0]))
        return int(res[0])

"""        stack = []
        ope = ["+", "-", "*", "/"]

        def handler(operator, a, b):
            if operator == "+":
                return a + b
            elif operator == "-":
                return a - b
            elif operator == "*":
                return a * b
            else:
                return int(a / b)

        for num in tokens:
            if num in ope:
                b = int(stack.pop())
                a = int(stack.pop())
                temp = handler(num, a, b)
                stack.append(int(temp))
            else:
                stack.append(int(num))
        print(stack[0])
        return stack[0]"""


if __name__ == '__main__':
    Test = Solution()
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    Test.evalRPN(tokens)
