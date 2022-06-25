#定义一个双链表结点
class DLNode(object):
    def __init__(self,data):
        self.data=data
        self.next=None
        self.pre=None

#定义一个双链表
class DLL(object):
    def __init__(self):
        #初始化头结点
        self.head=DLNode(None)

    #创建页码目录
    def createDLL(self):
        print('输入目录页码回车确认，结束输入“#”')
        cNode=self.head
        page=input('输入页码：')
        while page!='#':
            nNode=DLNode(int(page))
            cNode.next=nNode
            cNode=cNode.next
            page=input('输入页码：')
        print('页码目录创建成功！')


    #获取双链表长度
    def getLength(self):
        cNode=self.head
        length=0
        while cNode.next!=None:
            length+=1
            cNode=cNode.next
        return length

    #判空
    def isEmpty(self):
        if self.getLength()==0:
            return True
            print('为空')
        else:
            return False
            print('不为空')

    #遍历
    def travel(self):
        cNode=self.head
        if self.isEmpty():
            print('为空！')
            return
        while cNode.next!=None:
            if cNode.data==None:
                print('《上一页',end='')
            else:
                print('',cNode.data,'',end='')
            cNode=cNode.next
        print('',cNode.data,'',end='')
        print('下一页》')


    #前后翻页
    def turnPage(self):
        cNode=self.head.next
        print('当前位置页码：',cNode.data)
        print('N：向后翻页\n','P:向前翻页\n','Q:退出程序\n')
        order=input('输入：')
        while order!='Q':
            if order=='N':
                if cNode.next==None:
                    print('当前为 最后一页')
                else:
                    cNode=cNode.next
                    print('当前页码为：',cNode.data)
                order=input('输入：')
            elif order=='P':
                if cNode.pre==self.head:
                    print('当前为第一页')
                else:
                    cNode=cNode.pre
                    print('当前页码为：',cNode.data)
                order=input('输入:')
            else:
                print('输入有误，重新输入！')
                order=input('输入')


if __name__=='__main__':
    DL=DLL()
    DL.createDLL()
    DL.travel()
    DL.turnPage()
        
