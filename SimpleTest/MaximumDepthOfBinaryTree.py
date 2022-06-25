# @Time: 2022/6/15 9:56
# @Author: 丨枫
# @File MaximumDepthOfBinaryTree.py
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        # 遍历二叉树的每个结点，相加并将相加的结点存入列表
        # 若小于目标值则往下，若大于则回退，等于则退出
        # 采用先序遍历会比较方便，因为可以从根结点进行计算
        count_sum = 0
        res = []

        def preOrder(root):  # 先序遍历
            if root == None:
                return res
            if sum(res) < targetSum:  # 过小则先序遍历
                # print(root.val)
                print(sum(res))
                res.append(root.val)
                preOrder(root.left)
                preOrder(root.right)
            if sum(res) > targetSum:
                return
            if sum(res) == targetSum:
                return res
            return res

        resList = preOrder(root)
        return resList


if __name__ == '__main__':
    Test = Solution()
    root = [3, 9, 20, None, None, 15, 7]
