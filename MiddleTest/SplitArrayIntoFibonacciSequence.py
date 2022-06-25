# @Time: 2022/5/26 9:40
# @Author: 丨枫
# @File SplitArrayIntoFibonacciSequence.py
class Solution(object):
    def splitIntoFibonacci(self, num):
        """
        :type num: str
        :rtype: List[int]
        """
        # 直接排除长度小于3的字符串
        if len(num) < 3:
            return []

        def backtrack(cur, temp):  # cur标记当前位置，temp用于存储元素
            if len(temp) >= 3 and cur == n:  # 退出条件，当列表中有三个及以上的数构成斐波那契数列且当前位置是最后一位时跳出
                self.res = temp
                return
            if cur == n:  # 剪枝
                return
            for i in range(cur, n):
                if num[cur] == "0" and i > cur:  # 当数字以0开头时,应该跳过
                    return
                if int(num[cur: i + 1]) > 2 ** 31 - 1 or int(num[cur: i + 1]) < 0:  # 剪枝,排除超过范围的和不符合规范的数
                    continue
                if len(temp) < 2:
                    backtrack(i + 1, temp + [int(num[cur: i + 1])])
                else:
                    if int(num[cur: i + 1]) == temp[-1] + temp[-2]:  # 判断当前位置开始往后的数能否与暂存的列表中构成斐波那契数列
                        backtrack(i + 1, temp + [int(num[cur: i + 1])])  # 不能的话就进行回溯，将temp列表中的最后一个元素删除

        n = len(num)
        self.res = []
        backtrack(0, [])
        print(self.res)
        return self.res


if __name__ == '__main__':
    Test = Solution()
    num = "1101111"
    Test.splitIntoFibonacci(num)
