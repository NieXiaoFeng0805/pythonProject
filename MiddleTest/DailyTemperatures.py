# @Time: 2022/7/13 15:35
# @Author: 丨枫
# @File DailyTemperatures.py
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # 超时
        """
        res = []
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res.append(j - i)
                    break
                if (j == len(temperatures) - 1) and (temperatures[i] >= temperatures[j]):
                    res.append(0)
        res.append(0)
        print(res)"""

        # 超时
        """        
        left, right = 0, 1
        res = []
        while left < len(temperatures) - 1:
            if temperatures[right] > temperatures[left]:
                res.append(right - left)
                left += 1
                right = left + 1
                continue

            if right == len(temperatures) - 1:  # 到顶了还没找到
                res.append(0)
                left += 1
                right = left + 1
                continue
            right += 1
        print(res)
        res.append(0)
        return res"""

        answer = [0] * len(temperatures)
        stack = []
        for i in range(1, len(temperatures)):
            if temperatures[i] <= temperatures[-1]:
                stack.append(i)
            else:
                while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                    answer[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return answer


if __name__ == '__main__':
    Test = Solution()
    temperatures = [55, 38, 53, 81, 61, 93, 97, 32, 43, 78]
    Test.dailyTemperatures(temperatures)
