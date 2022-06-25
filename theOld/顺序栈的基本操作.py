class Stack(object):
    #初始化栈为最大空间为10的列表
    def __init__(self,Max):
        self.MaxSize=Max
        #提前构造一个固定大小的栈，初始化全为None
        self.stack=[None for x in range(0,self.MaxSize)]
        self.top=-1  #top指针

    #判空
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False

    #进栈
    def PushStack(self,x):
        if self.top<self.MaxSize-1:
            self.top+=1
            self.stack[self.top]=x
        else:
            print('栈满')
            return

    #出栈
    def popStack(self):
        if self.top==-1:
            print('栈空！')
            return
        else:
            #记住当前栈顶元素的值，然后栈顶的指针减一，返回出栈的元素
            iTop=self.top
            self.top-=1
            return self.stack[iTop]

    #获取栈顶元素
    def getTopStack(self):
        if self.isEmpty():
            print('栈空！')
        else:
            return self.stack[self.top]

    #以出栈的顺序遍历栈内元素
    def travelStack(self):
        if self.isEmpty():
            print('栈空')
            return
        itop=self.top
        while itop!=-1:
            #方法一直接调用弹出栈顶元素遍历，完成遍历后栈空！
            #print（self.popStack(),end=''）
            #方法三：
        #for i in range(0,)
            #方法二以top作为遍历到每一个元素的下标输出栈内每个元素值
            print(self.stack[itop],end='    ')
            itop-=1

    #获取顺序栈的长度
    def getLength(self):
        num=0
        for i in range(0,self.top+1):
            num +=1
        return num
    #键盘输入创建栈
    def createStack(self):
        data=input('输入元素，以“#”结束')
        while data!='#':
            self.PushStack(data)
            data=input('输入元素，以“#”结尾')

    #输出初始的栈以观察入栈和出栈的区别：
    def __str__(self):
        return '栈内元素为：'+str(self.stack)


    #测试
if __name__=='__main__':
    s=Stack(6)
    print('栈是否为空：',s.isEmpty(),'\n')
    s.createStack()
    print('栈内元素为：\n',s.stack)
    print(s.isEmpty(),'\n')
    print(s.getLength(),'\n')
    print('弹出的栈顶元素为：',s.popStack())
    print('栈的元素个数为：',s.getLength())
    print('栈顶元素为：',s.getTopStack(),'\n')
    print('栈的元素个数为：\n',s.getLength())
    print('栈内元素为：\n')
    s.travelStack()
    print(' ')
    print('栈的元素个数为：')
    print(s.getLength(),'\n')
        
        
