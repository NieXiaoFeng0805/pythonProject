# @Time: 2022/8/18 13:16
# @Author: 丨枫
# @File LongestSubstringWithoutRepeatingCharacters.py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 暴力
        """

        if len(s) < 2:
            return len(s)
        ans = 1  # 长度
        for i in range(len(s)):
            if ans >= len(s) - i:  # 当前最长子串已经大于剩余的子串，即后面不可能会出现比这更长的子串了
                print(ans)
                return ans
            noRepet = [s[i]]  # 存储不重复的字符
            for j in range(i + 1, len(s)):
                if s[j] in noRepet:  # 重复
                    break
                else:
                    noRepet.append(s[j])
            ans = max(ans, len(noRepet))"""
        # 滑动窗口
        if len(s) < 2:
            return len(s)
        L = 0  # 窗口左边界
        noRepet = set()  # 存储不重复字符
        n = len(s)
        ans = 0
        cur_len = 1  # 当前窗口长度
        for i in range(n):
            while s[i] in noRepet:  # 出现重复，移动窗口
                noRepet.remove(s[L])
                L += 1
                cur_len -= 1
            if cur_len > ans:
                ans = cur_len
            noRepet.add(s[i])
        return ans


if __name__ == '__main__':
    Test = Solution()
    Test.lengthOfLongestSubstring(s="abcabcbb")
