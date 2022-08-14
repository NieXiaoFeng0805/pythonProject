# @Time: 2022/8/11 11:18
# @Author: 丨枫
# @File ReformatTheString.py
class Solution:
    def reformat(self, s: str) -> str:
        if len(s) == 1:
            return s
        # 存放字母和数字
        numsTables = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        num_list, alpha_list = [], []
        for i in s:
            if i in numsTables:
                num_list.append(i)
            else:
                alpha_list.append(i)
        print(num_list, alpha_list)
        if abs(len(num_list) - len(alpha_list)) > 1:  # 必有两个字母或数字相邻
            return ''
        res = [0, 0]
        n_p, a_p = 1, 1  # 插入游标
        if len(num_list) < len(alpha_list):
            res[0], res[1] = alpha_list[0], num_list[0]
            for i in range(2, len(s)):
                if i % 2 == 0:  # 偶数添加字母
                    res.append(alpha_list[n_p])
                    n_p += 1
                else:
                    res.append(num_list[a_p])
                    a_p += 1
        else:
            res[0], res[1] = num_list[0], alpha_list[0]
            for i in range(2, len(s)):
                if i % 2 == 0:  # 偶数添加数字
                    res.append(num_list[n_p])
                    n_p += 1
                else:
                    res.append(alpha_list[a_p])
                    a_p += 1
        print(res)
        return ''.join(res)


if __name__ == '__main__':
    Test = Solution()
    Test.reformat(s="covid2019")
