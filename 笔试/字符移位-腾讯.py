# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/18 10:51
# software: PyCharm
"""
文件说明：
把一个字符串的大写字母放到字符串的后面，各个字符的相对位置不变，且不能申请额外的空间。
"""


def move_str(sub_str):
    """
    转为列表后再进行遍历
    碰到大写字母则记录下标，向字符串末尾添加该大写字母并将原来位置删除
    大写 65-90 小写 97-122
    :param n:
    :param sub_list:
    :return:
    """
    n = len(sub_str)
    sub_list = list(sub_str)
    for i in range(n):
        if 65 <= ord(sub_list[i]) <= 90:  # 大写字母
            sub_list.append(sub_list[i])  # 添加
            sub_list[i] = ''  # 删除
            i -= 1 if i != 0 else 0
    return "".join(sub_list)


while True:
    try:
        s = input()
        res = move_str(s)
        print(res)
    except EOFError:
        break
