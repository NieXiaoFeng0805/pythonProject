# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/18 10:28
# software: PyCharm
"""
文件说明：
给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？
输出需要删除的字符个数。
"""
import sys


class Solution:
    def create_str(self):
        str_list = []
        for line in sys.stdin:
            str_list.append(line)
        return str_list

    def solution(self):
        str_list = self.create_str()
        # print(str_list)
        for sub_str in str_list:


    def find_longest(self, num_list):
        '''
        构成回文子串有两种情况
            1、每个字符出现的次数都是偶数次
            2、有且只有一个字符出现的次数是奇数次

        :param num_list:
        :return:
        '''
        n = len(num_list)
        if n < 2:
            return num_list



Solution().solution()
