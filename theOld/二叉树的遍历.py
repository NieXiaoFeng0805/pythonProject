
#类说明：定义二叉树的一个结点
#类释义：有结点值data，该结点的左孩子 和 该结点的右孩子
class LinkedBinaryTreeNode(object):
    def __init__ (self):
        self.data = '#'
        self.LeftChild = None
        self.RightChild = None
    #先序遍历递归算法
    def PreOrder(self,Root):
        if Root is not None:
            self.VisitBinaryTreeNode(Root)
            self.PreOrder(Root.LeftChild)
            self.PreOrder(Root.RightChild)

    #访问二叉树的一个结点的函数
    def VisitBinaryTreeNode(self,BinaryTreeNode):
        #值为‘#’的结点代表空结点
        if BinaryTreeNode.data is not '#':
            print(BinaryTreeNode.data)

    #先序遍历的非递归算法

    #先序遍历二叉树的函数
    def NoPreOrder(self,Root):
        StackTreeNode = []
        tTreeNode = Root
        while len(StackTreeNode) > 0 or tTreeNode is not None:
            while tTreeNode is not None:
                
                StackTreeNode.append(tTreeNode)
                tTreeNode = tTreeNode.LeftChild
            if len(StackTreeNode) >0:
                tTreeNode = StackTreeNode.pop()
                self.VisitBinaryTreeNode(tTreeNode)
                tTreeNode = tTreeNode.RightChild

    #访问二叉树的一个结点的函数
    def VisitBinaryTreeNode(self,BinaryTreeNode):
        #值为‘#’的结点代表空结点
        if BinaryTreeNode.data is not '#':
            print(BinaryTreeNode.data)


    #中序遍历的递归算法

    #中序遍历二叉树的函数
    def InOrder(self,Root):
        if Root is not None:
            self.InOrder(Root.LeftChild)
            self.VisitBinaryTreeNode(Root)
            self.InOrder(Root.RightChild)


        #访问二叉树的一个结点的函数
    def VisitBinaryTreeNode(self,BinaryTreeNode):
        #值为‘#’的结点代表空结点
        if BinaryTreeNode.data is not '#':
            print(BinaryTreeNode.data)

    #中序遍历 的非递归算法
        #中序遍历二叉树的函数
    def NoInOrder(self,Root):
        StackTreeNode = []
        tTreeNode = Root
        while len(StackTreeNode) > 0 or tTreeNode is not None:
            while tTreeNode is not None:
                self.VisitBinaryTreeNode(tTreeNode)
                StackTreeNode.append(tTreeNode)
                tTreeNode = tTreeNode.LeftChild
            if len(StackTreeNode) >0:
                tTreeNode = StackTreeNode.pop()
                tTreeNode = tTreeNode.RightChild

        #访问二叉树的一个结点的函数
    def VisitBinaryTreeNode(self,BinaryTreeNode):
        #值为‘#’的结点代表空结点
        if BinaryTreeNode.data is not '#':
            print(BinaryTreeNode.data)


    #后续遍历 的递归算法
        #后续遍历二叉树的函数
    def PostOrder(self,Root):
        if Root is not None:
            self.InOrder(Root.LeftChild)
            self.InOrder(Root.RightChild)
            self.VisitBinaryTreeNode(Root)

        #访问二叉树的一个结点的函数
    def VisitBinaryTreeNode(self,BinaryTreeNode):
        #值为‘#’的结点代表空结点
        if BinaryTreeNode.data is not '#':
            print(BinaryTreeNode.data)

    #后续遍历 的非递归算法

    def NoPostOrder(self,Root):
        StackTreeNode = []
        tBinaryTreeNode = Root
        tTree = None
        while  tBinaryTreeNode is not None:
            tTree = TreeState(tBinaryTreeNode,0)
            StackTreeNode.append(tTree)
            tBinaryTreeNode = tBinaryTreeNode.LeftChild
        while len(StackTreeNode) >0:
            tTreeNode = StackTreeNode.pop()
            if tTree.BinaryTreeNode.RightChild is None or tTree.VisitedFlag == 1:
                self.VisitBinaryTreeNode(tTree.BinaryTreeNode)
            else:
                StackTreeNode.append(tTree)
                tTree.VisitedFlag =1
                tBinaryTreeNode = tTree.BinartTreeNode.RightChild
                while tBinaryTreeNode is not None:
                    tTree = TreeState(tBinaryTreeNode,0)
                    StackTreeNode.append(tTree)
                    tBinaryTreeNode = tBinaryTreeNode.LeftChild

        #访问二叉树的一个结点的函数
    def VisitBinaryTreeNode(self,BinaryTreeNode):
        #值为‘#’的结点代表空结点
        if BinaryTreeNode.data is not '#':
            print(BinaryTreeNode.data)
                    
        
