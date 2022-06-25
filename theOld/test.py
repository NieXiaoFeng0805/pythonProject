# -*- coding:utf-8 -*-
# @Time      :2020/11/12 23.04
# @Author    :Mr.Nie
# @Site      :
# @File      :University.py
# @Safeware  :PyCharm
# ——————————————————————————————————————

import bs4
import requests
import openpyxl
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup


def getHTMLTxt(url):  # 获取目标页面
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }

    r = requests.get(url, headers=headers, timeout=30)
    r.encoding = r.apparent_encoding
    return r.text


def fillUnivList(ulist, html, clearlist, grouplist):  # 解析和筛选数据，去除空格，返回数据列表
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].find('a').string, tds[2].string, tds[3].string])

    for i in ulist:
        for j in i:
            lis = str(j)
            lis = lis.strip()
            clearlist.append(lis)

    for i in range(0, len(clearlist), 4):
        grouplist.append(clearlist[i:i + 4])

    return grouplist


def inputExcel(ws, List, num, year):  # 输入表格
    for j in range(num):
        u = List[j]
        u.insert(0, year)
        ws.append(u)

    ws.append(["", "", "", "", ""])


uList = []
clearList = []
groupList = []

url_2020 = r"https://www.shanghairanking.cn/rankings/bcur/202011"
url_2019 = r"https://www.shanghairanking.cn/rankings/bcur/201911"
url_2018 = r"https://www.shanghairanking.cn/rankings/bcur/201811"

html_2020 = getHTMLTxt(url_2020)
html_2019 = getHTMLTxt(url_2019)
html_2018 = getHTMLTxt(url_2018)

# 清空列表
uList.clear()
clearList.clear()
groupList.clear()  
data_2020 = fillUnivList(uList, html_2020, clearList, groupList)[0:10]

 # 清空列表
uList.clear()
clearList.clear()
groupList.clear() 
data_2019 = fillUnivList(uList, html_2019, clearList, groupList)[0:10]

# 清空列表
uList.clear()
clearList.clear()
groupList.clear()  
data_2018 = fillUnivList(uList, html_2018, clearList, groupList)[0:10]

# 输出到表格中
fn = r"C:\Users\FBI OPENTHDOOR\Desktop\大学排名表.xlsx"
wb = openpyxl.Workbook()  # 创建工作簿
ws = wb.worksheets[0]
ws.title = "中国大学排名信息"  # 更改表的名称
ws.append(["年份", "排名", "学校名称", "省份", "类型"])  # 添加表头信息

inputExcel(ws, data_2020, 10, 2020)
inputExcel(ws, data_2019, 10, 2019)
inputExcel(ws, data_2018, 10, 2018)

wb.save(fn)  # 保存工作簿

# 绘图
l = []
level = []
year = [2020, 2019, 2018]


def getNob(list_year, name):  # 获取对应学校名次

    l = []
    for i in list_year:
        for j in i:
            lis = str(j)
            l.append(lis)

    level.append(l[l.index(name) - 1])
    return level


def paint(name):
    level.clear()
    level_paint_2020 = getNob(data_2020, name)[0]
    level_paint_2019 = getNob(data_2019, name)[1]
    level_paint_2018 = getNob(data_2018, name)[2]

    level_paint = [level_paint_2020, level_paint_2019, level_paint_2018]
    print(level_paint)
    plt.plot(year, level_paint)
    plt.title(name)
    plt.show()



