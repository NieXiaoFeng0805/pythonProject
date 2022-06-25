class LBinTreeNode(object):         #初始化根结点#
    def __init__(self,data='#',lchild = None, rchild = None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

        #后序遍历要先遍历根结点找到最左的结点，但这些根结点不输出，要用一个标志位来区分这些结点是否被访问。


class BinTreeState(object):
    def __init__(self,LBinTreeNode,Flag):
        self.LBinTreeNode = LBinTreeNode
        self.Flag = Flag

class LBinTree(object):     #左根树#
    def __init__(self,root = None):
        self.root = root

    def createBinTree(self,T):  #建立只含根结点的树#
        item = input('输入前序遍历的值：')
        if item == '#':
            T = None
        else:
            T = LBinTreeNode(item)
            T.lchild = self.createBinTree(T.lchild)
            T.rchild = self.createBinTree(T.rchild)
        return T

    def breadTrave(self,T):     #层序遍历#
        if T ==None:
            return
        queue = [T]
        while queue:
            cnode = queue.pop(0)
            print(cnode.data,end = '')

            if cnode.lchild != None:
                queue.append(cnode.lchild)
            if cnode.rchild != None:
                queue.append(cnode.rchild)

    def preorder(self,T):       #用递归实现前序遍历#
        if T == None :
            if T == None:
                return
            else:
                print(T.data,end='')
                self.preorder(T.lchild)
                self.preorder(T.rchild)

    def Norder(self,T):         #非递归实现中序遍历#
        stackBinTreeNode = []
        #结点初始值为node
        cNode = node
        while len(stackBinTreeNode) > 0 or cNode != None:
            while cNode != None:
                stackBinTreeNode.append(cNode)
                cNode = cNode.lchild

            if len(stackBinTreeNode) >0:
                cNode = stackBinTreeNode.pop()
                print(cNode.data,end = '')
                cNode = cNode.rchild

    def Lorder(self,T):     #非递归实现后续遍历#
        stackBinTreeNode = []
        cNode = None
        #结点被访问标志，初始值为None
        sNode = None
        while cNode != None:
            sNode = BinTreeState(cNode,0)
            stackBinTreeNode.append(sNode)
            cNode = cNode.lchild
        while len(stackBinTreeNode) >0:
            sNode = stackTreeNode.pop()
            if sNode.LBinTreeNode.rchild == None or sNode.Flag == 1:
                print(sNode.LBinTreeNode.data,end = '')
            else:
                stackBinTreeNode.append(sNode)
                sNode.Flag = 1
                cNode = sNode.LBinTreeNode.rchild
                while cNode != None:
                    sNode = BinTreeNode.append(sNode,0)
                    stackBinTreeNode.append(sNode)
                    cNode = cNode.lchild


tree = LBinTree()
t = tree.createBinTree(tree.root)
print('前序遍历的结果是：',end = '')
tree.preorder(t)

print('\n')

print('层序遍历的结果是：',end ='')
tree.breadTrave(t)


print('\n')

print('中序遍历的结果是：')
tree.Norder(t)

print('\n')

print('后序遍历的结果是：')
tree.Lorder(t)




                   
