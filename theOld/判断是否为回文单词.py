#父类
class Stack(object):
    def __init__(self,Max):
        self.MaxSize=Max
        self.x=[None for x in range(0,self.MaxSize)]
        self.top=-1

    #判空
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    #进栈
    def inStack(self,item):
        if self.top<self.MaxSize-1:
            self.top+=1
            self.x[self.top]=item
        else:
            print('栈满！')
            return
    #出栈
    def outStack(self):
        if self.top==-1:
            print('栈空！')
            return
        else:
            #记住当前栈顶元素的值，然后栈顶的指针减一，返回出栈的元素
            iTop=self.top
            self.top-=1
            return self.x[iTop]

    #获取栈顶元素
    def getStack(self):
        if self.isEmpty():
            print('栈空！')
            return
        else:
            return self.x[self.top]

    #遍历
    def travelStack(self):
        if self.isEmpty():
            print('栈空！')
            return
        itop=self.top
        while itop!=-1:
            print(self.outStack(),end='   ')
            itop-=1

    #创建栈
    def createStack(self):
        data=input('输入元素：  结束按“#”')
        while data!='#':
            self.inStack(data)
            data=input('输入元素：')

    #输出初始栈以观察入栈和出栈的区别
    def __str__(self):
        return '栈内元素为：' +str(self.x)

    #类的继承
class TestStack(Stack):
    def __init__(self,Max):
        super().__init__(Max)

    def plaindrome(self,str):
        S1=Stack(20)
        S2=Stack(20)
        i=0
        print('栈S1内的元素依次为：',end='')
        

    #输入的单词从前往后依次入栈形成S1
        while i<(len(str)):
            S1.inStack(str[i])
            print(str[i])
            i+=1
        print('S1内的元素依次为：',end='' )
            

        i-=1
        while i<(len(str)) and i>=0:
            S2.inStack(str[i])
            print(str[i])
            i-=1
        print('S2内的元素依次为：',end='' )

        #依次比较两个栈弹出的元素是否相等
        while S1.isEmpty()!=True:
            if S1.outStack()!=S2.outStack():
                print('元素不相等，',str,'不是回文单词')
                return
        print('栈空，S1与S2的元素完全相同，',str,'是回文单词')

    #测试
    def Test(self):
        str=input('输入第一个单词：')
        i=0
        while i<(len(str)):
            if (str[i]>='a' and str[i]<='z') or (str[i]>='A' and str[i]<='Z'):
                i+=1
            else:
                break
        if i==len(str):
            self.plaindrome(str)
        else:
            print('输入错误！')

if __name__=='__main__':
    TPD=TestStack(20)
    TPD.Test()
        
        
