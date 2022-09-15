# @Time: 2022/9/6 14:07
# @Author: 丨枫
# @File Reformat Date.py
class Solution:
    def reformatDate(self, date: str) -> str:
        dateList = date.split(" ")
        # print(dateList)
        monthlist = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        monthDict = dict(zip(monthlist, range(1, 13)))
        # print(monthDict)
        days = dateList[0]
        month = dateList[1]
        year = dateList[2]
        res = year + '-'
        for i in monthDict:
            if i == month and monthDict[i] < 10:
                res += '0' + str(monthDict[i])
            elif i == month and monthDict[i] >= 10:
                res += str(monthDict[i])
        res += '-'
        if len(days) == 3:
            res += '0' + days[0:1]
        if len(days) == 4:
            res += days[0:2]
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    Test.reformatDate(date="6th Jun 1933")
