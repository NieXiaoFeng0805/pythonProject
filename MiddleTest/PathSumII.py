# @Time: 2022/6/16 15:39
# @Author: 丨枫
# @File PathSumII.py
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self, root=None):
        self.root = root

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        # 遍历二叉树的每个结点，相加并将相加的结点存入列表
        # 若小于目标值则往下，若大于则回退，等于则退出
        # 采用先序遍历会比较方便，因为可以从根结点进行计算
        count_sum = targetSum
        res = []
        self.DFS(self, root, count_sum, res, [])
        return res

    def DFS(self, root, count_sum, res, path):
        if not root:  # 空结点
            return
        if not root.left and not root.right:  # 叶子结点
            if count_sum == root.val:  # 剩余的值等于叶子节点说明刚好合适
                res.append(path + [root.val])  # 将路径存入结果
        # 递归
        self.DFS(root.left, count_sum - root.val, res, path + [root.val])  # 遍历左子树
        self.DFS(root.right, count_sum - root.val, res, path + [root.val])  # 遍历右子树


if __name__ == '__main__':
    Test = Solution()
    root = [5, 4, 11, 2]
    print(sum(root))
