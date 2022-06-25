#循环序列队列的基本操作

class Queue(object):
    #初始化最大空间为Max的列表
    def __init__(self,Max):
        self.MaxSize=Max
        self.s=[None]*Max
        self.front=0
        self.rear=0

    def getLength(self):
        return (self.rear-self.front+self.front+self.MaxSize)%self.MaxSize

    #判空
    def isEmpty(self):
        if self.front==self.rear:
            return True
        else:
            return False

    #入队
    def inQueue(self,x):
        if (self.rear+1)%self.MaxSize!=self.front:
            self.s[self.rear]=x
            self.rear=(self.rear+1)%self.MaxSize

        else:
            print('队列已满！')
            return

    #出队
    def outQueue(self):
        if self.rear==self.front:
            print('队列为空！')
        else:
            data=self.s[self.front]
            self.s[self.front]=None
            self.front=(self.front+1)%self.MaxSize
            return data

    def createQueue(self):
        data=input('输入入列元素：（继续回车确认，结束“#”确认)')
        while data!='#':
            self.inQueue(data)
            data=input('输入入列元素：')

    def showQueue(self):
        for i in range(self.MaxSize):
            print(self.s[i],end='   ')
        print('')

if __name__=='__main__':
    Q=Queue(10)
    Q.createQueue()
    Q.showQueue()
    print('____________________________________________________________________')
    Q.inQueue ('long')
    Q.showQueue()
    print('____________________________________________________________________')
    Q.inQueue('short')
    Q.showQueue()
    print('____________________________________________________________________')
    for i in range (3):
        Q.outQueue()
    Q.showQueue()
    
