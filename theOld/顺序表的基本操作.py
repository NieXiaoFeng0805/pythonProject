#创建顺序表的实现
class SequenceList(object):
    def __init__(self):         #初始化顺序表函数#
        self.SeqList=[]         #创建顺序表并将其置空#

    #创建顺序表函数
    def CreateSequenceList(self):
        print("----------------------------------")
        print("输入数据后回车确认，结束输入“#”")
        print(" ")

        Element = input("输入元素")         #输入数据元素并存入顺序表中#
        while Element != '#':
            self.SeqList.append(int(Element))       #调用append（）方法在当前顺序表尾端直接插入新元素#
            Element = input("输入元素")
        print("顺序表创建成功")
    #查找元素的函数#
    def FindElement(self):
        key = input('输入查找的元素：')
        if key in self.SeqList:
            ipos = self.SeqList.index(SeqList,key)          #调用index（） 方法实现在列表中查找与数据元素key相匹配的值及其下标位置#
            print("查找成功 ， 值为：",self.SeqList[ipos],"的元素位于",ipos+1,"的位置")

        else:
            print("查找失败","当前顺序表中不存在值为：",key,"的元素")

    #指定位置插入函数#
    def InsertElement(self):
        ipos = int(input('输入待插入元素的位置'))
        Element = int(input('输入插入的元素'))
        self.SeqList.insert(ipos,Element)           #调用insert（，）方法将对象Element插入指定位置ipos#
        print("插入元素后。当前顺序表为：\n",self.SeqList)

    #指定位置删除函数#
    def DeleteElement(self):
        dpos = int(input("输入删除元素的位置"))
        print("正在删除")
        self.SeqList.remove(self.SeqList[dpos])         #调用remove方法，将指定位置dpos 上 的元素删除#
        print("删除元素后的顺序表为：\n",self.SeqList)

    #遍历顺序表函数#
    def TraverseElement(self):
        SeqListLen = len(self.SeqList)      #调用len（）方法，获得顺序表的长度#
        print("-------遍历顺序表中的元素----------")
        for i in range(0,SeqListLen):              #range() 方法，表明循环将被执行SeqListLen次#
            print("第",i+1,"个元素为：",self.SeqList[i])

if __name__ =='__main__':
    L = SequenceList()
    L.CreateSequenceList()
    L.TraverseElement()
    L.FindElement()
    L.InsertElement()
    L.DeleteElement()
    L.TraverseElement()
