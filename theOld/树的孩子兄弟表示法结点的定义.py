#定义树的一个结点
#分别放有数据data 、第一个孩子结点pFistChild 和 下一个兄弟结点pNextSibling
class TreeNode(object):
    def __init__ (self):
        self.data='#'
        self.pFirstChild = None
        self.pNextSibling = None
