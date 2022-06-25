#初始化结点函数#
class Node(object):
    def __init__(self,data):
        self.data = data        #创建数据域并初始化为data#
        self.next = None            #创建指针域初始化为 None#

#初始化头结点函数#
class SingleLinkedList(object):
    def __init__(self):
        self.head = Node(None)      #创建一个结点将其初始化为空 并且传给单链表的头结点#

    #创建单链表#
    def CreateSingleLinkedList(self):
        print("输入数据回车确认，结束输入“#”")
        print('________________________________')
        cNode = self.head       #变量cNode指向头结点#
        Element = input("输入当前结点的值")
        while Element != '#':
            nNode = Node(int(Element))      #输入的值作为参数去创建并初始化一个新结点（依次创建数据域为Element 的 Node类 结点）#
            cNode.next = nNode              #cNode 的next域中存入新结点的地址（当前结点的指针域存入新结点的地址）#
            cNode = cNode.next              #将cNode 指向cNode的后继结点（新插入的结点）#
            Element = input("输入当前结点的值")

    #尾插法#
    def InsertElementTail(self):
        Element =(input('输入待插入结点的值：'))
        if Element = '#':
            return

        cNode = self.head
        nNode = Node(int(Element))          #输入的值作为参数去创建并初始化一个新结点#
        while cNode.next != None:
            cNode = cNode.next              #最终将当前指针指向单链表的最后一个结点#
        cNode.next = nNode              #将结点nNode的地址存入最后一个结点的指针域#

    #头插法
    def InsertElementHead(self):
        Element = input("输入插入结点的值：")
        if Element == '#':
            return

        cNode = self.head
        nNode = Node(int(Element))      #输入的值作为参数去创建并初始化一个新结点#
        
        nNode.next = cNode.next     #将新结点的next域指向cNode的后继结点#
        cNode.next = nNode          #将nNode结点的地址存入cNde所指结点的指针域中#

    #查找指定元素并返回其位置#
    def FindElement(self):
        pos = 0         #指示当前下标的位置#
        cNode = self.head
        key = int(input("输入要查找的元素"))
        if self.IsEmpty():
            print('单链表为空')
            return

        while cNode.next != None and cNode.data!= key:
            cNode = cnode.next
            pos +=1
        if cNode.data == key:
            print("查找成功",key,"位于该链表的第",pos,"个位置上")
        else:
            print("查找失败")


    #输出单链表某一元素#

    def VisitElement(self,tNode):
        if tNode != None:
            print(tNode.data,"->",end='')
        else:
            print("None")
