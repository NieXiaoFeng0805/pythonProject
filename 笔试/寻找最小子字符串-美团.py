# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/16 16:34
# software: PyCharm
"""
文件说明：
给出 母字符串 STR1（不为空） ，存在另一个字符串STR2（可为空）；
需要从STR1中找到包含STR2中所有字符的最小子串STR3
"""

import collections


class Solution:
    def create_num(self):
        f_str, child_str = input(), input()
        return f_str, child_str

    def judge(self, child_dict):
        # 判断是否完全包含str2
        for i in child_dict:
            if child_dict[i] != 0:  # 说明没有全部包含
                return False
        return True

    def so(self):
        fstr, chstr = self.create_num()
        if not chstr:
            return fstr
        child_dict = collections.Counter(chstr)
        index_list = []
        min_i, max_i = 0, 0
        for i, ch in enumerate(fstr):
            if ch in child_dict and child_dict[ch] != 0:
                index_list.append(i)  # 记录下标
                min_i = min(min_i, i)
                max_i = max(max_i, i)
                child_dict[ch] -= 1
        # 判断是否完全包含
        flag = self.judge(child_dict)
        if flag:
            # 完全包含,则最小子串的下标已知
            print(fstr[min_i:max_i + 1])
        else:
            print("")


def demo(str1, str2):
    if len(str2) < 1:
        return str1
    source = [0] * 255
    target = [0] * 255
    start = 0
    left = -1
    right = len(str1)
    match = 0
    length = len(str1)

    for char in str2:
        target[ord(char)] += 1

    for i in range(len(str1)):
        source[ord(str1[i])] += 1
        if target[ord(str1[i])] >= source[ord(str1[i])]:
            match += 1

        if match == len(str2):
            while start < i and source[ord(str1[start])] > target[ord(str1[start])]:
                source[ord(str1[start])] -= 1
                start += 1

            if i - start < length:
                length = i - start
                left = start
                right = i

            source[ord(str1[start])] -= 1
            match -= 1
            start += 1

    return "" if left == -1 else str1[left:right + 1]


if __name__ == "__main__":
    a,b = input().split()
    print(demo(a, b))

# Solution().so()
