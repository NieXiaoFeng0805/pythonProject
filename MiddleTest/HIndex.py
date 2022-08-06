# @Time: 2022/8/2 11:07
# @Author: 丨枫
# @File HIndex.py


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """
        if len(citations) == 1:
            return 1 if citations[0] >= 1 else 0
        # 先排序
        citations.sort()
        for i in range(len(citations)):
            h = len(citations) - i  # 满足条件的论文数
            if h <= citations[i]:  # 找到相对较大的h
                print(h)
                return h
        return 0
        """

        # 优化
        citations.sort(reverse=True)
        for i, t in enumerate(citations):
            if i >= t: return i
        return len(citations)


if __name__ == '__main__':
    Test = Solution()
    citations = [3, 0, 6, 1, 5]
    Test.hIndex(citations)
