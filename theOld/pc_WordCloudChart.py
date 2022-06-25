import requests
from bs4 import BeautifulSoup
from urllib import request
import bs4
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt



#得到网页
def getHTMLText(url):
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.67'
    }
    try:

        r = requests.get(url,headers=headers,timeout=30)   #获取网页
        r.encoding = r.apparent_encoding    #得到编码方式
        return r.text    #得到文本
    except:
        print("异常")
        
#操作网页,爬取相应数据
def fillUnivList(html,attr):

    soup = BeautifulSoup(html,"html.parser")    #解析网页
    
    
    #获取标题
    tag1=soup.select('h1')   #寻找h1标签
    print("文章标题为：",tag1[0].text)  #获取标签内文本

    #获取图片，并把他们存入相应文件夹下
    for image in soup.find_all('img',id='{BE009ED4-1763-46AD-B951-9988573C4EBC}'):   #获取id
        value=image.get(attr)    #获取src属性值
        value='http://www.qstheory.cn/wp/2020-11/17/'+value         #拼接src属性值
        print(value)                                                        
        request.urlretrieve(value,r'C:\Users\FBI OPENTHDOOR\Desktop\1805200422_聂晓龙\picture.jpg')  #将图片存入文件夹，重命名：picture.jpg


        
        #获取文章内容并写入目标文件
    artical=soup.find_all('p')
    file=open(r'C:\Users\FBI OPENTHDOOR\Desktop\1805200422_聂晓龙\text.txt','w')
    for i in artical:
        file.write(i.get_text().strip())
    file.close()    #关闭

#
def WordCloudChar():
    excludes={"进一步","我们"}
    txt=open(r'C:\Users\FBI OPENTHDOOR\Desktop\1805200422_聂晓龙\text.txt','r').read()
    words = jieba.lcut(txt)     #分词
    counts = {}     #存储词语及其出现的次数
    c=[]
    for word in words:
        if len(word) == 1:
            continue
        elif word=="习近平" or word=="主席":
            rword="习近平"
        else:
            rword=word
        counts[rword] = counts.get(rword, 0) + 1    # 遍历词语，每出现一次加 1
    for word in excludes:
        del counts[word]
        items = list(counts.items())
        items.sort(key=lambda x: x[1], reverse=True)    #排序

    for i in range(40):
        word, count = items[i]
        print("{0:<5}{1:>5}".format(word, count))
        c.append(word)
    text=" ".join(c)


    w=WordCloud(width=800,height=600,font_path="msyh.ttc",background_color="blue",max_words=40,)
    w.generate(text) #生成词云
    plt.imshow(w)    #形成词云图
    plt.axis('off')  #不显示坐标
    plt.show()        #显示词云图
    w.to_file("pc_WordCloudChart.png")  #词云输出图像文件




if __name__ =='__main__':

    url = r"http://www.qstheory.cn/wp/2020-11/17/c_1126749191.htm"  #目标网址
    getHTMLText(url)    #传入参数
    html = getHTMLText(url)
    fillUnivList(html,'src')    #传入参数
    WordCloudChar() #调用
    

   


        
