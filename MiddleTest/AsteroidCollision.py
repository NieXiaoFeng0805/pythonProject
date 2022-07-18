# @Time: 2022/7/14 10:57
# @Author: 丨枫
# @File AsteroidCollision.py
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # 设置一个栈，指针移动将值入栈，随后与栈顶元素进行对比
        # 若是同方向则入栈，不同方向则进行当前元素和栈顶元素绝对值的比较,有三种情况
        # 必须是左边大于0右边小于0才能碰撞

        stack = []
        p = 0
        while p < len(asteroids):
            if len(stack) != 0:  # 栈不空
                if stack[-1] > 0 and asteroids[p] < 0:  # 会碰撞
                    if abs(asteroids[p]) == stack[-1]:  # 绝对值相等
                        stack.pop()  # 栈顶元素删除
                        p += 1
                        continue
                    elif abs(asteroids[p]) < stack[-1]:  # 当前值小于栈顶元素
                        p += 1
                        continue
                    else:  # 当前值大于栈顶元素
                        stack.pop()  # 弹出栈顶元素
                        continue  # 继续判断
                else:  # 不会碰撞
                    stack.append(asteroids[p])  # 添加元素
                    p += 1
                    continue

            else:
                stack.append(asteroids[p])
            p += 1
        print(stack)
        return stack


if __name__ == '__main__':
    Test = Solution()
    asteroids = [5, 10, -5]
    Test.asteroidCollision(asteroids)
