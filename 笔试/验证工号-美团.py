# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/9 10:29
# software: PyCharm
"""
文件说明：
18位数字组成字符串，规则包括
1. 前六位 由键盘输入
2. 7-14位代表是出生日期，范围是1900.01.01-2023.12.31
3. 15-17位代表是哪个组，不能是完全一样的3位数字
4. 18位是一位的校验和，假设是 x ，则需要满足
(x+a_1+a_2+a_3+a_4+...+a_17) % 8 = 1 ，a_1-a_17 代表了前面的17位数字
"""


class Solution:
    def define_code(self):
        flag = False
        ver_part, ver_num = self.create_num()
        for num in ver_num:
            if self.ver_part(ver_part, num):  # 判断部门
                flag = True
            # 判断出生日期
            elif self.ver_bri(num):
                flag = True
            # 判断组
            elif self.judge_group(num):
                flag = True
            # 校验和
            elif self.last_num(num):
                pass
            else:
                flag = True

            if flag:
                print("error")
            else:
                print("ok")

    def ver_part(self, ver_part, ver_num):
        if ver_num[:6] not in ver_part:  # 错误
            return True

    def ver_bri(self, l):
        year = l[6:10]
        month = l[10:12]
        days = l[12:14]
        if month == '02' and days == '29':
            if self.judge_year(int(year)):
                return False  # 是闰年
            else:
                return True
        elif int(month) > 12 or int(month) < 1:  # 越界
            return True
        else:
            return False

    def judge_group(self, l):
        if len(set(l)) == 1:
            return True

    def last_num(self, l):
        num_list = [int(d) for d in l]
        if sum(num_list) % 8 == 1:
            return True
        else:
            return False

    def judge_year(self, year):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        else:
            return False

    def create_num(self):
        n = int(input())
        partiment = []
        for i in range(n):
            partiment.append(input())

        m = int(input())
        verify_num = []
        for j in range(m):
            verify_num.append(input())
        return partiment, verify_num


if __name__ == '__main__':
    Solution().define_code()
