class Node(object):
    #初始化结点
    def __init__(self,data):
        self.data=data
        #data用来存放元素
        self.next=None
        #next用来存放下一个结点的地址


class HeadLink(object):
    #初始化头结点
    def __init__(self):
        self.head=Node(None)


#创建一个单链表
    def createSLL(self):
        print('请输入数据后回车确认，若结束请按’#‘...')
        cNode = self.head
        Element=input('请输入当前结点的值')
        while Element!='#':
            nNode=Node(int(Element))
            cNode.next=nNode
            cNode=cNode.next
            Element=input('请输入当前结点的值：')
        print('单链表SLL创建完成')


    #判空
    def isEmpty(self):
        if self.getLenth()==0:
            print('为空')
        else:
            print('不为空')

    #获取元素个数
    def getLenth(self):
        cur=self.head
        count=0
        while cur.next!=None:
            count+=1
            cur=cur.next
        return count
        print('元素的个数为:',count)
        
    def Print(self):
        cre=self.head
        while cre != None:
            print(cre.data,'->',end='')
            cre=cre.next
        print('#')

        #指定位置插入
    def ChaRu(self):
        pos=int(input('请输入要插入的位置'))
        if pos<=0:
            self.ChaRuhead()
            #若指定位置pos为第一个元素前，则执行头插法

        elif pos>(self.getLenth()-1):
            self.ChaRutail()

        else:
            count=0
            pre=self.head
            Element=input('请输入要插入的元素')
            if Element=='#':
                return
            nNode=Node(int(Element))
            while count<pos-1:
                pre=pre.next
                count+=1
#将新节点的链接域指向位置节点
            nNode.next=pre.next
            pre.next=nNode
            print('结点',Element,'插入成功')

#头插法
    def TouCha(self):
        Element=input('执行头插法，请输入要插入的元素')
        if Element=='#':
            return
        cNode=self.head
        nNode=Node(int(Element))
        nNode.next=cNode.next
        cNode.next=nNode

#删除元素
    def Delete(self):
        ditem=int(input('输入要删除的元素的值'))
        cur=self.head
        pre=None
        while cur != None:
            #找到指定元素
            if cur.data==ditem:
                #若第一个就是待删除的结点
                if not pre:
                    #将头指针指向后一个结点
                    self.head=cur.next
                else:
                    #将删除位置的前一个结点的next指向删除位置后一结点
                    pre.next=cur.next
                    break
            else:
                #继续后移寻找元素
                pre=cur
                cur=cur.next
        if cur==None:
            print('没有找到此元素！')

#查并返回其位置
    def Find(self):
        pos=0
        cur=self.head
        key=int(input('输入要查找的元素值'))
        while cur!=None:
            if cur.data==key:
                print('查找成功,值为：',key,'位于当前链表第',pos,'个位置')
                break
            else:
                cur=cur.next
                pos+=1
        if cur==None:
            print('查找失败，当前列表中不存在值为',key,'的值')
        
                
            

if __name__=='__main__':
    SLL=HeadLink()
    SLL.createSLL()
    SLL.Print()
    print(SLL.isEmpty())
    print(SLL.getLenth())
    SLL.ChaRu()
    SLL.Print()
    SLL.TouCha()
    SLL.Print()
    SLL.Delete()
    SLL.Print()
    SLL.Find()
    SLL.Print()
