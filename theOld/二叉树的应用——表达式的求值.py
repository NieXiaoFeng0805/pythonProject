#二叉树的应用——表达式的求值
#二叉树的连式存储
#二叉链表上的二叉树基本操作


#中缀表达式  例：3+4  后缀：34+  前缀：+34

#中缀转换为后缀
class InfixExpression(object):
    def __init__(self,expression):
        self.InfixExpression = expression.spilt('')
        self.PostfixExpression = []

    #中缀转后缀的算法
    def InfixToPsotfix(self):
        operator = []
        for item in self.InfixExpression:
            if item in ['+','-','*','/']:
                while len(operator) >= 0:
                    if operator == 0:
                        operator.append(item)
                        break
                    tmp = operator.pop()
                    if tem == '(' or self.Grade(item) > self.Grade(tmp):
                        operator.append(tmp)
                        operator.append(item)
                        break
                    else:
                        self.PostfixExpression.append(tmd)
            elif item == ')':
                operator.append(item)
            elif item == ')' :
                while len(operator) > 0:
                    tem = operator.pop()
                    if tmp!='(':
                        self.PostfixExpression.append(tmp)
                    else:
                        break
            else:
                self.PostfixExpression.append(operator.pop())

        while len(operator) > 0:
            self.PostfixExpression.append(operator.pop())

    #返回运算符的运算级的函数
    def Grade(self,operator):
        if operator == '+':
            return 1
        elif operator == '-':
            return 1
        elif operator == '*':
            return 2
        elif operator == '/':
            return 2


#定义一个二叉树结点，分别拥有左孩子，右孩子 ，和数据

class LinkedBinaryTreeNode(object):
    def __init__ (self):
        self.data = '#'
        self.LeftChild = None
        self.RightChild = None

#定义一个二叉树，根据一个后缀表达式建立一颗二叉树

class BinaryTree(BinaryTreeNode):
    def __init__ (self,PostfixExpression):
        self.PostfixExpression = PostfixExpression

    #由后缀表达式创建的一颗二叉树
    def CreatePostfixBinaryTree(self,Root):
        StackTreeNode = []
        for item in self.PostfixExpression:
            if item in ['+','-','*','/']:
                OperandTwo = StackTreeNode.pop()
                OperandOne = StackTreeNode.pop()
                RootNode = LinkedBinaryTreeNode()
                RootNode.data = item
                RootNode.LeftChild = OperandOne
                RootNode.RightChild = OperandTwo
                StackTreeNode.append(RootNode)
            else:
                TreeNode = LinedBinaryTreeNode()
                TreeNode.data = item
                StackTreeNode.append(TreeNode)
        TreeNode = StackTreeNode.pop()
        Root.data = TreeNode.data
        Root.LeftChild = TreeNode.LeftChild
        Root.RightChild = TreeNode.RightChild
        print('二叉树创建成功！')

    #先序遍历得到前缀表达式的算法
    def GetPrefixExpression(self,BinaryTree,expression):
        if BinaryTree is not None:
            self.GetPrefixExpression(BinaryTree.LeftChild,expression)
            self.GetPrefixExpression(BinaryTree.RightChild,expression)
            self.VisitBinaryTree(BinaryTree,expression)

    #先序遍历二叉树得到前缀表达式
    def PreOrder(self,BinaryTree,expression):
        if BinaryTree is not None:
            self.VisitBinaryTree(BinaryTree,expression)
            self.PreOrder(BinaryTree.LeftChild,expression)
            self.PreOrder(BinaryTree.RightChild,expression)

    #访问二叉树的一个结点
    def VisitBinaryTree(self,BInaryTree,expression):
        print(str(BinaryTree.data)+' ',end = "")
        expression = expression.append(BinaryTree.data)

#定义用于对后缀表达式求值
class PostfixExpression(object):
    def __init__ (self):
        self.result = ''

    #前缀表达式求值的算法
    def GetValue(self,PostfixExpression):
        StackValue = []
        for item in PostfixExpression:
            if item in ['+','-','*','/']:
                operand2 = StackValue.pop()
                operand1 = StackValue.pop()
                result = self.Calculation(operand1,operand2,item)
                StackValue.append(result)
            else:
            StackValue.append(int(item))
        self.result = str(StackValue[0])

    #进行四则运算的函数
    def Calculation(self,operand1,operand2,operator):
        if operator = '+':
            return operand1 + operand2
        if operator = '-':
            return operand1-operaend2
        if operator = '*':
            return operand1 * operand2
        if operator = '/':
            return operand1 / operand2


#定义用于对前缀表达式求值
class PrefixExpression(object):
    def __init__(self):
        self.result = None

    #前缀表达式求值函数
    def GetValue(self,expression):
        StackValue = []
        index = len(expression)-1
        while index >=0:
            if expression[index] in ['+','-','*','/']:
                OperandOne = StackValue.pop()
                OperandTwo = StackVa;ue.pop()
                result = self.Caculation(OperandOne,OperandTwo,expression[index])
                if result is 'error':
                    print('除数不能为0')
                    return
                StackValue.append(result)
            else:
                StackValue.appennd(int(expression[index]))
            index -= 1
        result = StackValue.pop()
        self.result = result

    #进行四则运算的函数
    def Calculation(self,OperandOne,OperandTwo,operator):
        if operator == '+':
            return OperandOne + OperandTwo
        elif operator == '-':
            return OperandOne - OperandTwo
        elif operator == '*':
            return OperandOne * OperandTwo
        elif operator == '/':
            if OperandTwo == 0:
                return 'error'
            else:
                return OperandOne / OperandTwo

    def __init__(self,InfixExpression):
        self.InfixExpression = InfixExpression


    #由中缀表达式创建的二叉树的函数
    def CreateBinaryTree(self,Root):
        StackOperator = []
        StackTreeNode = []
        for item in self.InfixExpression:
            if item in ['+','-','*','/']:
                if len(StackOperator) >0 and item in ['+','-']:
                    Operand2 = StackTreeNode.pop()
                    Operand1 = StackTreeNode.pop()
                    RootNode = LinkedBinaryTreeNode()
                    RootNode.data = StackOperator.pop()
                    RootNode.LeftChild = Operand1
                    RootNode.RightChild = Operand2
                    StackTreeNode.append(RootNode)
                    StackOperator.append(item)
                else:
                    StackOperator.append(item)
            else:
                TreeNode = BinaryTreeNode()
                TreeNode.data = item
                StackTreeNode.append(TreeNode)


            while len(StackOperator) >0:
                RootNode = BinaryTreeNode()
                RootNode.RightChild = StackTreeNode.pop()
                RootNode.LeftChild = StackTreeNode.pop()
                StackTreeNode.append(RootNode)
            Root.data = StackTreeNode[0].data
            Root.LeftChild = StackTreeNode[0].LeftChild
            Root.RightChild = StackTreeNode[0].RightChild

    #后序遍历二叉树，得到后缀表达式
    def PostOrder(self,BinaryTree,expression):
        if BinaryTree is not None:
            self.PostOrder(BinaryTree.LeftChild,expression)
            self.PostOrder(BinaryTree.RightChild,expression)
            silf.VisitBinaryTree(BinaryTree,expression)

    #先序遍历二叉树，得到前缀表达式
    def preOrder(self,BinaryTree,expression):
        if BinaryTree is not None:
            self.VisitBinaryTree(BinaryTree,expression)
            self.PreOrder(BinaryTree.LeftChild,expression)
            self.PreOrder(BinaryTree.RightChild,expression)

    #访问一个二叉树结点
    def VisitBinaryTree(self,BinaryTree,expression):
        print(str(BinaryTree.data)+' ',end = "")
        expression = expression.append(str(BinaryTree.data))


#计算中缀表达式的值
expression = '9 + (3-1)*3+10/2'
print('题目所给中缀表达式为：')
print('expression')

#将中缀表达式转换为后缀表达式
iexpression = InfixExpression(expression)
iexpression.InfixToPostfix()
print('转换之后的后缀表达式为：')
print(''.join(iexpression.PostfixExpression))


#根据后缀表达式创建一颗二叉树
print('由后缀表达式创建二叉树！')
bt = BinaryTree(iexpression.PostfixExpression)
root = LinkedBinaryTreeNode()
bt.CreateBinaryTree(root)


#前序遍历二叉树得到前缀表达式
expression = []
print('前序遍历二叉树得到的表达式如下：')
bt.PreOrder(root,expression)

#计算并输出前缀表达式的结果
pexpression = PrefixExpression()
pexpression.GetValue(expression)
print('/n'+'运算结果：'+str(pexpression.result))
