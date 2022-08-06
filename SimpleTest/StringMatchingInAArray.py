# @Time: 2022/8/6 11:04
# @Author: 丨枫
# @File StringMatchingInAArray.py
class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        # 按长度排个序
        words = sorted(words, key=len)
        res = []
        for i in range(len(words)):
            for j in range(i, len(words)):
                if words[i] in words[j] and words[i] != words[j]:
                    if words[i] in res:
                        continue
                    res.append(words[i])

        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    words = ["leetcoder", "leetcode", "od", "hamlet", "am"]
    Test.stringMatching(words)
