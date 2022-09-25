# @Time: 2022/9/17 15:40
# @Author: 丨枫
# @File Largest Substring Between Two Equal Characters.py
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        new_s = [i for i in s]
        print(new_s)
        if len(new_s) == len(set(new_s)):
            return -1
        res = 0
        l, r = 0, 1
        while res < len(s) - l:
            if new_s.count(s[l]) == 1:
                l += 1
                continue
            else:
                index_l = l
                index_r = s.rfind(s[l])
                res = max(res, index_r - index_l - 1)
                l += 1
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    Test.maxLengthBetweenEqualCharacters(s="mgntdygtxrvxjnwksqhxuxtrv")
