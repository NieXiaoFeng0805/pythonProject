#双链表的基本操作

#定义一个双链表的结点
class DoubleLinkedNode(object):
    #初始化结点
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
        
#定义一个双链表
class DoubleLinkList(object):
    #初始化头结点
    def __init__(self):
        self.head=DoubleLinkedNode(None)

    #创建双链表
    def createDoubleLinkList(self):
        print('*************************************************\n')
        print('*请输入结点的值按回车确认，若想结束请输入“#”*。')
        print('*************************************************')
        cNode=self.head
        item=input('请输入结点的值：')
        while item!='#':
            nNode=DoubleLinkedNode(int(item))
            cNode.next=nNode
            nNode.prev=cNode
            cNode=cNode.next
            item=input('请输入结点的值：')
        print('双链表 DLL 创建成功！')

    #获取双链表的长度
    def getLength(self):
        length=0
        cNode=self.head
        while cNode.next!=None:
            length+=1
            cNode=cNode.next 
        return length

    #判断双链表是否为空
    def isEmpty(self):
        if self.getLength()==0:
            return True
        else:
            return False

    #尾插法插入结点 
    def insertItemInTail(self):
        item=input('请输入要插入结点的值：')
        while item=='#':
            return
        nNode=DoubleLinkedNode(int(item))
        cNode=self.head
        while cNode.next!=None:
                cNode=cNode.next
        nNode.prev=cNode
        cNode.next=nNode
        print('结点',item,'插入成功！')

    #头插法插入结点
    def insertItemInHead(self):
        item=input('请输入要插入结点的值：')
        if item=='#':
            return
        nNode=DoubleLinkedNode(int(item))
        pNode=self.head

        if self.isEmpty():
            nNode.prev=pNode
            pNode.next=nNode
            print('结点',item,'插入成功！')
        else:
            #保存头结点原来的后继结点
            cNode=pNode.next
            #1 新节点 prev 变为头结点
            nNode.prev=pNode
            #2 头结点后继结点改为新结点
            pNode.next=nNode
            #3 新节点的后继结点为原来头结点的后继结点
            nNode.next=cNode
            #4原来头结点后继结点的前驱结点变为新结点
            cNode.prev=nNode
            print('结点',item,'插入成功！')

    #在任意指定位置插入结点
    def insertItem(self):
        pos=int(input('请输入要插入结点的位置：'))
        #若指定位置 pos 为第一个元素之前，则执行头插法插入到链表头部
        if pos<=0:
            self.insertItemInHead()
        #若指定位置超过链表尾部，则执行尾插法插入到链表的尾部
        elif pos>(self.getLength()-1):
            self.insertItemInTail()
        else:
            item=input('请输入要插入结点的值：')
            if item=='#':
                return
            nNode=DoubleLinkedNode(int(item))
            pNode=self.head
            cNode=self.head
            length=0
            while length<pos:
                pNode=cNode
                length+=1
                cNode=cNode.next
            nNode.prev=pNode
            pNode.next=nNode
            nNode.next=cNode
            cNode.prev=nNode
            print('结点',item,'插入成功！')

    #删除指定位置结点
    def removeItem(self):
        pos=int(input('请输入要删除节点的位置：'))
        if pos<=0 or pos>(self.getLength()-1):
            print('输入的位置有误，请重新输入！')
            pos=int(input('请输入要删除节点的位置：'))
        else:
            length=0
            cNode=self.head
            pNode=self.head
            while length<pos:
                length+=1
                pNode=cNode
                cNode=cNode.next
            qNode=cNode.next
            pNode.next=qNode
            qNode.prev=pNode
            del cNode
            print('成功删除第',pos,'个位置的结点！')

    #删除指定值的结点
    def deleteItem(self):
        key=input('请输入要删除节点的值为：')
        if key=='#':
            return
        cNode=self.head
        pNode=self.head
        if self.isEmpty():
            print('当前双向链表为空！')
            return
        while cNode.next!=None and cNode.data!=int(key):
            pNode=cNode
            cNode=cNode.next
        if cNode.data==int(key):
            qNode=cNode.next
            qNode.prev=pNode
            pNode.next=qNode

            del cNode
            print('成功删除值为',key,'的结点!')
        else:
            print('删除失败！双向链表中没有值为',key,'的结点')

    #按指定值查找结点并返回其位置
    def findItem(self):
        length=0
        cNode=self.head
        item=int(input('请输入要查找结点的值：'))
        if self.isEmpty():
            print('当前双向链表为空！')
            return
        while cNode.next!=None and cNode.data!=item:
            length+=1
            cNode=cNode.next
        if cNode.data==item:
            print('查找成功！值为',item,'的结点位于该双向链表的第',length,'个位置')
        else:
            print('查找失败！当前双向链表中不存在值为',item,'的结点')

    #按照 next 域遍历双向链表
    def travelDoubleLinkListBN(self):
        cNode=self.head
        print('按照 next 域遍历带头结点的双向链表：')
        if self.isEmpty():
            print('当前双向链表为空！')
            return
        while cNode.next!=None:
            print('<-',cNode.data,'->',end='')
            cNode=cNode.next
        print('<-',cNode.data,'->',end='')
        print(None)

    #测试函数
    def printOut(self):
        print('################################################')
        print('####### 基础实验 4 实现双向链表的基础操作 #######')
        while 1:
            print('############## 双向链表的操作类型 ##############\n',
                  '1 双向链表初始化；\n','2 判断链表是否为空；\n',
                  '3 创建双向链表；\n','4 统计双向链表元素个数；\n',
                  '5 任意位置插入元素；\n','6 尾部插入元素；\n',
                  '7 头部插入元素；\n','8 删除指定位置结点；\n',
                  '9 删除指定值的结点；\n','10 查找指定值的结点；\n',
                  '11 退出操作；\n','*************************************\n')
            num=int(input('请输入你要操作的类型号（输入对应数字）：'))
            if num==1:
                print('\n(1)初始化双向链表 DLL：',end=' ')
                try:
                    self.__init__()
                    print('双向链表 DLL 初始化成功！')
                except:
                    print('双向链表 DLL 初始化失败！')
            elif num==2:
                print('\n(2)判断当前双向链表是否为空：',end=' ')
                try:
                    self.isEmpty()
                    print('当前双向链表为空！')
                except:
                    print('当前双向链表不为空！')
            elif num==3:
                print('\n(3)创建双向链表 DLL：')
                try:
                    self.createDoubleLinkList()
                    self.travelDoubleLinkListBN()
                except ValueError:
                    print('输入有误，请重新输入！')
                    self.createDoubleLinkList()
                    self.travelDoubleLinkListBN()               
            elif num==4:
                print('\n(4)双向链表 DLL 的元素个数为:',end=' ')
                try:
                    print(self.getLength())
                except:
                    print('获取 DLL 中元素个数出错！')
            elif num==5:
                print('\n(5)将指定值的结点插入至 DLL 中的指定位置')
                try:
                    self.insertItem()
                    self.travelDoubleLinkListBN()                  
                except:
                    print('插入结点 49 出错！')
            elif num==6:
                print('\n(6)用尾插法将指定值的结点插入至 DLL 中')
                try:
                    self.insertItemInTail()
                    self.travelDoubleLinkListBN()                   
                except:
                    print('尾端插入结点出错！')
            elif num==7:
                print('\n(7)用头插法将指定值的结点插入至 DLL 中')
                try:
                    self.insertItemInHead()
                    self.travelDoubleLinkListBN()                   
                except:
                    print('尾端插入结点出错！')
            elif num==8:
                print('\n(8)删除 DLL 中指定位置的结点')
                try:
                    self.removeItem()
                    self.travelDoubleLinkListBN()                    
                except:
                    print('删除指定位置结点出错！')
            elif num==9:
                print('\n(9)删除 DLL 中指定值的结点')
                try:
                    self.deleteItem()
                    self.travelDoubleLinkListBN()
                except:
                    print('删除指定值结点出错！')
            elif num==10:
                print('\n(10)查找 DLL 中指定值的结点')
                try:
                    self.findItem()
                except:
                    print('查找结点出错！')
            elif num==11:
                break

if __name__=='__main__':
    DLL=DoubleLinkList()
    DLL.printOut()            
            
                    
                
            
            
            
                
            

        

    
        

