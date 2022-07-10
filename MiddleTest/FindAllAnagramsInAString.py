# @Time: 2022/7/4 13:49
# @Author: 丨枫
# @File FindAllAnagramsInAString.py
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # 旧
        """        
        # 将p 拆分
        p_list = []
        p_list.extend(i for i in p)
        print(p_list)

        # 以p_list的长度遍历s，若该长度中的字符有一个不在p_list中，则将首字符索引+1，进入下一个子串
        res = []
        i = 0
        while (i + len(p_list)) <= len(s):
            arr = p_list.copy()  # 对p_list进行浅复制
            for j in range(i, i + len(p_list)):
                if p in s[i:i+len(p_list)]:
                    res.append(i)
                    break
                if s[j] not in arr:  # 出现子串中没有的立即返回
                    break
                else:
                    arr.remove(s[j])
            if arr == []:  # 可以组成异位串
                res.append(i)
            i += 1
        print(res)
        return res"""
        # 优化
        """        
        # 设置双指针标记左窗口和右窗口边界、valid记录有效值
        left, right, valid = 0, 0, 0
        res = []
        # 设置字符计数字典，分别记录s中需要的字符和p中已有的字符
        needs = {i: p.count(i) for i in p}  # 子串需要的字符
        # print(needs)
        windows = {i: 0 for i in p}  # 窗口中包含子串的字符数
        # print(windows)
        while right < len(s):  # 当右指针到末尾结束
            temp = s[right]  # 临时存储
            # 更新窗口内数据
            if temp in needs.keys():  # 找到需要的字符
                windows[temp] += 1
                if windows[temp] == needs[temp]:  # 需要的字符已找到
                    valid += 1
            right += 1  # 窗口右边界右移
            # print("window: [%d, %d)", left, right)
            # 判断窗口左边界是否需要收缩
            while (right - left) >= len(p):  # 窗口长度大于所需字符串的长度，需缩减；等于则添加索引
                # 当窗口符合条件时
                if valid == len(needs):
                    res.append(left)
                temp1 = s[left]
                left += 1
                if temp1 in needs.keys():
                    if windows[temp1] == needs[temp1]:
                        valid -= 1
                    windows[temp1] -= 1
        print(res)
        return res"""
        # 再次尝试

        n, m, res = len(s), len(p), []
        if n < m: return res  # 不和要求

        p_cnt = [0] * 26  # p中出现的字符次数
        s_cnt = [0] * 26  # s中出现的字符次数

        for i in range(m):  # 计算p中出现的字符次数
            p_cnt[ord(p[i]) - ord('a')] += 1

        left = 0  # 窗口左边界
        for right in range(n):
            cur_right = ord(s[right]) - ord('a')
            s_cnt[cur_right] += 1
            while s_cnt[cur_right] > p_cnt[cur_right]:
                cur_left = ord(s[left]) - ord('a')
                s_cnt[cur_left] -= 1
                left += 1
            if right - left + 1 == m:
                res.append(left)
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    s = "cbaebabacd"
    p = "abc"
    Test.findAnagrams(s, p)
