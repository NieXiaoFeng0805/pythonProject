#定义树的根结点
#分别放有结点值data 和 该结点的第一个孩子结点FirstChild
class TreeNode(object):
    def __init__ (self):
        self.data='#'
        self.FirstChild = None

#定义一个孩子结点
#包括该结点在数组中的下标 index 及某一个兄弟结点 NextSibling

class ChildNode(object):
    def __init__(self):
        self.index = -1
        self.NextSibling = None
