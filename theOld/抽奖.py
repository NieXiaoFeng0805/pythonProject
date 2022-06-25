#循环单链表运用--抽奖
import random
class CLNode(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class CSLL(object):
    def __init__(self):
        self.head=CLNode(None)

    def createCSLL(self):
        print('输入“传彩球”决赛名单，回车确认，结束输入“#”')
        cNode=self.head
        item=input('输入传彩球的名单：')
        while item!='#':
            nNode=CLNode(item)
            cNode.next=nNode
            nNode.next=self.head
            cNode=cNode.next
            item=input('输入“传彩球”的决赛名单：')
        print('当前参与的人数为：',self.getLength(),'分别是：')
        
    def getLength(self):
        cNode=self.head
        length=0
        if cNode.next==None:
            return length
        while cNode.next!=self.head:
            length+=1
            cNode=cNode.next
        return length

    def isEmpty(self):
        if self.getLength()==0:
            return True
        else:
            return False

    def travel(self):
        cNode=self.head
        if self.isEmpty():
            print('为空！')
            return
        while cNode.next!=self.head:
            #不输出头结点
            if cNode.data==None:
                print('')
                cNode=cNode.next
            else:
                print(cNode.data,'->',end='')
                cNode=cNode.next
        print(cNode.data)
        


    def Lottery(self):
        pNode=self.head
        cNode=self.head.next
        count=self.getLength()
        total=self.getLength()
        while count!=1:
            import random
            randomNum=random.randint(0,10)
            print("第",(total-count)+1,"轮抽取的随机数为：",randomNum)
            transNum=randomNum % count
            while transNum!=0:
                pNode=pNode.next
                cNode=cNode.next
                transNum=transNum-1
            if cNode==self.head:
                cNode=cNode.next
                pNode=pNode.next
                print("被淘汰的会员为：",cNode.data)
                pNode.next=cNode.next
                del cNode
                cNode = pNode.next
                count=self.getLength()
            cNode=self.head.next
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print("最终获奖的是：",cNode.data)

if __name__=='__main__':
    C=CSLL()
    C.createCSLL()
    C.travel()
    C.Lottery()
