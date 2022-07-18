# @Time: 2022/6/15 10:24
# @Author: 丨枫
# @File BinaryTree.py
class BinaryTree:
    def __init__(self, value):  # 初始化二叉树
        self._left = None
        self._right = None
        self._value = value

    def insertLeftChild(self, value):  # 创建左子树
        if self._left:
            print("左子树已存在")
        else:
            self._left = BinaryTree(value)  # 赋值
            return self._left

    def insertRightChild(self, value):  # 创建右子树
        if self._right:
            print("右子树已存在")
        else:
            self._right = BinaryTree(value)  # 赋值
            return self._right

    def Show(self):  # 打印函数
        print(self._value)

    def preOrder(self, countL, countR):  # 前序遍历
        print(self._value)  # 输出根结点的值q

        if self._left:
            countL += 1
            self._left.preOrder(countL, countR)  # 遍历左子树
        if self._right:
            countR += 1
            self._right.preOrder(countL, countR)  # 遍历右子树

    def postOrder(self):  # 后续遍历
        if self._left:
            self._left.postOrder()
        if self._right:
            self._right.postOrder()
        print(self._value)

    def inOrder(self):  # 中序遍历
        if self._left:
            self._left.inOrder()
        print(self._value)
        if self._right:
            self._right.inOrder()

    # def levelOrder(self): # 层次遍历


if __name__ == '__main__':
    root = BinaryTree('root')
    a = root.insertLeftChild('A')
    b = root.insertRightChild('B')
    c = a.insertLeftChild('C')
    d = c.insertRightChild('D')
    e = b.insertRightChild('E')
    f = e.insertLeftChild('F')
    countL, countR = 0, 0
    root.preOrder(countL, countR)
