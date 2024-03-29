# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/2/26 18:11
# software: PyCharm
"""
文件说明：

"""


# 10进制转二进制
def ten_to_binary(num):
    return bin(num)


# 10进制转16进制
def ten_to_hex(num):
    return hex(num)


# 十进制转八进制
def ten_to_oct(num):
    return oct(num)


# 其他转十进制
def other_to_ten(num):
    return int(num)


# if __name__ == '__main__':
#     num = 20
#     print("10->2", ten_to_binary(num))
#     print("10->8", ten_to_oct(num))
#     print("10-16", ten_to_hex(num))
#     print("other->ten", other_to_ten(num))

if __name__ == '__main__':
    l1 = [3, 4, 5]
    l2 = [3, 9, 1]
    l = ''.join(l1)
    print()
