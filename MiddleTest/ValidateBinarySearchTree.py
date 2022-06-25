# @Time: 2022/6/14 12:49
# @Author: 丨枫
# @File ValidateBinarySearchTree.py
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 用中序遍历的思想，将树的所有结点值存入列表
        # 观察结果可知，若是二叉搜索树，则遍历的结果一定是按升序排列的
        # 若结果列表中的数不是升序则说明二叉搜索树无效
        # 判断是否升序
        res = []

        def Traversal(root):
            if root == None:
                return False
            # 中序遍历
            Traversal(root.left)
            print(root.val)
            res.append(root.val)
            Traversal(root.right)
            return res

        # 比较是否为升序
        resList = Traversal(root)
        for i in range(1, len(resList)):
            if resList[i] <= resList[i - 1]:
                return False
        return True


if __name__ == '__main__':
    Test = Solution()
