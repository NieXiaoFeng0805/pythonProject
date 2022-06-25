#运动会队形变换

class StudentNode(object):
    #初始化节点
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
        self.next=None


class SLL(object):
    
    #初始化头节点
    def __init__(self):
        self.head=StudentNode(None,None)



    #创建学生单链表A
    def createStudentSLL(self):
        print('请输入数据后按回车确认，若结束请输入 ‘#’')
        cNode=self.head
        item=input('请输入姓名、性别并用回车确认')
        while item!='#':
            Name=item.split(' ')[0]
            Sex=item.split(' ')[1]
            nNode = StudentNode(Name,Sex)
            
            #节点向后移动
            cNode.next=nNode
            cNode=cNode.next

            item=input('请输入姓名、性别并用空格隔开')
        print('单链表创建成功')



#判断链表是否为空
    def isEmpty(self):
        if self.getLength()==0:
            return True
        else:
            return False


#获取列表元素的个数
    def getLength(self):
        length=0
        cNode=self.head
        while cNode.next!=None:
            length+=1
            cNode=cNode.next            #游标向后移动
        return length


#拆分链表为男生链表和女生链表
    def divideSLL(self,LinkedListB,LinkedListC):
        aNode=self.head
        bNode=LinkedListB.head
        cNode=LinkedListC.head
        pos=0

        #遍历一边A的每个节点
        while aNode.next!=None:
            aNode=aNode.next
            pos+=1
            pNode=aNode
        #对每一个节点判断所在位置是奇数（男）还是偶数（女）
        #提取相应节点构造男生链表B和女生链表C
            if pos%2==1:
                bNode.next=pNode
                bNode=bNode.next
            else:
                cNode.next=pNode
                cNode=cNode.next


        #构造A和C的未结点
        bNode.next=None
        cNode.next=None


    #遍历链表
    def travelSLL(self):
        cNode=self.head
        pos=0
        if self.isEmpty():
            print('该链表为空')
            return

        while cNode.next!=None:
            if pos==0:
                print('序号','|''姓名','|''性别','\n')
            else:
                print(pos,'|',cNode.name,'|',cNode.sex,'\n')
            cNode=cNode.next
            pos+=1


        print(pos,'|',cNode.name,'|',cNode.sex,'\n')


#测试函数
    def printSLL(self):
        cNode=self.head.next
        if cNode.sex=='男':
            
            print('男生小分队包含',self.getLength(),'个人,分别是：')
            self.travelSLL()
        else:
            print('女生小分队包含',self.getLength(),'个人，分别是：')
            self.travelSLL()
        


if __name__=='__main__':
    LA=SLL()
    LB=SLL()
    LC=SLL()
    LA.createStudentSLL()
    LA.travelSLL()
    LA.divideSLL(LB,LC)
    LB.printSLL()
    LC.printSLL()
