# @Time: 2022/8/31 14:43
# @Author: 丨枫
# @File Validate Stack Sequences.py
class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        list_in = []
        for i in pushed:
            list_in.append(i)  # 入栈
            while list_in[-1] == popped[0]:  # 需要出栈
                popped.pop(0)
                list_in.pop()
                if len(popped) == 0:  # 当出栈列表为空说明有这个入栈顺序
                    return True
                if len(list_in) == 0:  # 当新列表为空则将下一个数入栈(此时popped列表不为空)
                    break
        return False


if __name__ == '__main__':
    Test = Solution()
    Test.validateStackSequences(pushed=[1, 0], popped=[1, 0])
