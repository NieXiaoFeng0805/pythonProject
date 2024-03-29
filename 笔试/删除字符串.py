# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/8 19:52
# software: PyCharm
"""
文件说明：

"""


def delete_consecutive_chars(s):
    stack = []  # 初始栈
    for char in s:  # 遍历字符串
        if stack and char == stack[-1]:  # 若栈中有元素且出现重复
            stack.pop()  # 弹出元素
        else:  # 否则添加元素到栈中
            stack.append(char)

    result = ''.join(stack)
    return result if result else "no"


# 读取多组输入并输出
while True:
    try:
        s = input()
        result = delete_consecutive_chars(s)
        print(result)
    except EOFError:
        break
