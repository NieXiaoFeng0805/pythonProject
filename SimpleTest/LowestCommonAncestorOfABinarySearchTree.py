# @Time: 2022/6/17 11:55
# @Author: 丨枫
# @File LowestCommonAncestorOfABinarySearchTree.py
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 两次遍历
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 因为是二叉搜索树，利用其特性；创建两条路径，用于存放遍历到两个目标节点的路径
        # 将这两条路径从后往前遍历，对比情况
        # 利用二叉树的性质，左边小右边大，若目标值小于当前结点值则在左子树，反之则在右子树
        path1 = []
        path2 = []
        path1 = self.Order(root, p)
        path2 = self.Order(root, q)
        anc = None
        for i, j in zip(path1, path2):
            if i == j:
                anc = i
            else:
                break
        return anc

    # 遍历
    def Order(self, root, tar):
        path = []  # 用于存储路径
        treeNode = root  # 赋值
        while treeNode != tar:  # 遍历
            path.append(treeNode)  # 存值
            if tar.val < treeNode.val:  # 利用搜索二叉树的特性，左边小，右边大
                treeNode = treeNode.left
            else:
                treeNode = treeNode.right
        path.append(treeNode)  # 目标恰好等于结点值
        return path


# 一次遍历
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        anc = root
        while True:
            if p.val < anc.val and q.val < anc.val:  # 两目标值都小于目前结点
                anc = anc.left  # 祖先结点应该在左边
            elif p.val > anc.val and q.val > anc.val:  # 两目标值都大于目前结点
                anc = anc.right  # 祖先结点应该在右边
            else:
                break
        return anc
