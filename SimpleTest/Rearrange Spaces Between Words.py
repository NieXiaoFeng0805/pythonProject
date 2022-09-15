# @Time: 2022/9/7 11:58
# @Author: 丨枫
# @File Rearrange Spaces Between Words.py
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()  # 提取单词
        print(words)
        space = text.count(' ')  # 计算空格的个数
        print(space)
        if len(words) == 1:
            return words[0] + ' ' * space
        per_space, rest_space = divmod(space, len(words) - 1)  # 把除数和余数运算结果结合起来，返回一个包含商和余数的元组（a//b,a%b）。
        return (' ' * per_space).join(words) + ' ' * rest_space


if __name__ == '__main__':
    Test = Solution()
    Test.reorderSpaces(text=" practice   makes   perfect")
