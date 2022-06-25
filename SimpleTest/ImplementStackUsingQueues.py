# @Time: 2022/5/31 9:28
# @Author: 丨枫
# @File ImplementStackUsingQueues.py


class MyStack:

    def __init__(self):
        self.StackList = []  # 创建列表对象

    def push(self, x: int) -> None:
        self.StackList.append(x)  # 添加元素

    def pop(self) -> int:
        resTop = self.StackList[len(self.StackList) - 1]  # 将后入的元素赋值给临时变量
        self.StackList.pop(len(self.StackList) - 1)  # 移除顶部元素
        return int(resTop)

    def top(self) -> int:
        resTop = self.StackList[len(self.StackList) - 1]  # 将后入的元素赋值给临时变量
        return int(resTop)

    def empty(self) -> bool:
        if len(self.StackList)==0:
            return True
        else:
            return False


if __name__ == '__main__':
    Test = MyStack()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
