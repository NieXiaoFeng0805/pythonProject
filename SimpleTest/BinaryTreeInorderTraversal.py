# @Time: 2022/6/13 10:50
# @Author: 丨枫
# @File BinaryTreeInorderTraversal.py

class Solution(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def Traversal(root):
            if root == None:
                return False
            # 中序遍历
            Traversal(root.left)

            Traversal(root.right)
            res.append(root.val)
            return res
        resList = Traversal(root)
        # ##
        # 颜色标记法
        # 使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
        # 如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
        # 如果遇到的节点为灰色，则将节点的值输出。
        # WHITE, GRAY = 0, 1
        # res = []
        # stack = [(WHITE, root)]
        # while stack:
        #     color, node = stack.pop()
        #     if node is None: continue
        #     if color == WHITE:
        #         stack.append((WHITE, node.right))
        #         stack.append((GRAY, node))
        #         stack.append((WHITE, node.left))
        #     else:
        #         res.append(node.val)
        # return res


if __name__ == '__main__':
    Test = Solution()
    root = [1, None, 2, 3]
    Test.inorderTraversal(root)
