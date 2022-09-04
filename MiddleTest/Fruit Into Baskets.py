# @Time: 2022/8/31 16:04
# @Author: 丨枫
# @File Fruit Into Baskets.py
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        if len(fruits) == 1:
            return 1
        # 初始化
        i, j = 0, 0
        res = 0
        classMap = defaultdict(int)
        classCnt = 0

        # 移动滑窗右边界
        while j < len(fruits):
            # 判断当前是否满足条件
            if classMap[fruits[j]] == 0:
                classCnt += 1
            classMap[fruits[j]] += 1

            # 若不满足条件，移动i
            while classCnt > 2:
                if classMap[fruits[i]] == 1:
                    classCnt -= 1
                classMap[fruits[i]] -= 1
                i += 1

            # 一旦满足条件，更新结果
            res = max(res, j - i + 1)
            j += 1
        print(res)
        return res


if __name__ == '__main__':
    Test = Solution()
    Test.totalFruit(fruits=[3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4])
