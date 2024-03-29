# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/20 17:14
# software: PyCharm
"""
文件说明：

"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(node):
    '''
    前序遍历  根 左 右
    :return:
    '''
    if node:
        print(node.value)
        print(preorder(node.left))
        print(preorder(node.right))


def inorder(node: TreeNode):
    '''
    中序遍历  左 根 右
    :param node:
    :return:
    '''
    if node:
        print(inorder(node.left))
        print(node.value)
        print(inorder(node.right))


def postorder(node: TreeNode):
    '''
    后序遍历 左 右 根
    :param node:
    :return:
    '''
    if node:
        print(postorder(node.left))
        print(postorder(node.right))
        print(node.value)


if __name__ == '__main__':
    # 示例用法
    # 创建二叉树节点
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # 调用前序遍历函数
    # preorder(root)
    # inorder(root)
    postorder(root)
