# @Time: 2022/7/10 16:01
# @Author: 丨枫
# @File ImplementQueueUsingStacks.py


class MyQueue(object):

    def __init__(self):
        self.stack_in = []  # 存放输入元素
        self.stack_out = []  # 存放输出元素

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)  # 压栈

    def pop(self):
        """
        :rtype: int
        """
        res = self.stack_in[-1]
        self.stack_in.pop()  # 弹出
        return res

    def peek(self):
        """
        :rtype: int
        """
        return self.stack_in[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack_in) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
if __name__ == '__main__':
    Test = MyQueue()
    Test.push()
