#创建循环单链表

class Node(object):
    def __init__(self,data):
        self.data=data      #存储元素
        self.next=None      #用来存放下一个结点的标识

#定义循环单链表
class CycleList(object):
    #初始化头结点
    def __init__(self):
        self.head=Node(None)
        #创建循环单链表
    def createCycleList(self):
        print('输入数据后按回车确认，结束按“#”')
        #设置一个游标始终指向链表最后一个元素
        cNode=self.head
        item=input('输入当前结点的值：')
        while item!='#':
            nNode=Node(int(item))
            cNode.next=nNode
            nNode.next=self.head
            cNode=cNode.next
            item=input('输入当前结点的值：')
        print('循环单链表创建完成！')


        #判空
    def isEmpty(self):
        if self.getLength()==0:
            return True
            print('该链表为空')
        else:
            return False
            print('该链表不为空')

        #获取列表长度
    def getLength(self):
        cNode=self.head
        length=0
        if cNode.next==None:
            return length
        while cNode.next!=self.head:
            length+=1
            cNode=cNode.next
        return length


        #头插
    def insertHead(self):
        item=input('输入要插入的值：#')
        if item=='#':
            return
        #将原来链表中头结点的位置交给新结点
        #新结点的链接域 next 指向头接待你
        cNode=self.head
        nNode=Node(int(item))
        nNode.next=cNode.next
        cNode.next=nNode
        #尾插
    def insertTail(self):
        item=input('执行尾插法，输入要插入的值：')
        if item=='#':
            return
        cNode=self.head
        while cNode.next!=self.head:
            cNode=cNode.next
        nNode=Node(int(item))
        cNode.next=nNode
        nNode.next=self.head

        
    #指定位置插入结点
    def insert(self):
        pos=int(input('输入要插入的位置：'))
        if pos<=0:
            self.insertHead()
        elif pos>(self.getLength()-1):
            self.insertTail()
        #找到指定位置
        else:
            length=0
            cNode=self.head
            item=input('输入要插入的数：')
            if item=='#':
                return
            nNode=Node(int(item))
            while length<pos-1:
                length+=1
                cNode=cNode.next
                #将新结点的链接域指向插入位置结点
            nNode.next=cNode.next
            cNode.next=nNode
            print('结点',item,'插入成功')




        #删除指定位置的结点
    def deleteitem(self):
        ditem=int(input('输入要删除结点的值：'))
        cNode=self.head
        pNode=self.head
        if self.isEmpty():
            print('当前链表为空')
            return
        while cNode.next!=self.head and cNode.data!=ditem:
            pNode=cNode
            cNode=cNode.next
        if cNode.data==ditem:
            pNode.next=cNode.next
            del cNode
            print('成功删除值为',ditem,'的结点')
        else:
            print('删除失败,不存在值为',ditem,'的结点')


            #查找并返回位置
    def finditem(self):
        pos=0
        cNode=self.head
        key=int(input('输入要查找的值：'))
        if self.isEmpty():
            print('当前链表为空')
            return
        while cNode.next!=self.head and cNode.data!=key:
            cNode=cNode.next
            pos+=1
        if cNode.data==key:
            print('查找成功，值为：',key,'位于该循环链表的第：',pos,'个位置')
        else:
            print('查找失败！当前循环链表中不存在值为：',key,'的结点')

            #遍历循环单链表
    def travel(self):
        cNode=self.head

        if self.isEmpty():
            print('当前循环链表为空')
            return
        while cNode.next!=self.head:
            
            print(cNode.data,'=>',end='')
            cNode=cNode.next
        print(cNode.data,'=>',end='')
        print('头结点')


        





if __name__=='__main__':
    CSLL=CycleList()

    CSLL.createCycleList()
  
    CSLL.insert()
 
    CSLL.deleteitem()
    CSLL.finditem()
    CSLL.travel()

  
