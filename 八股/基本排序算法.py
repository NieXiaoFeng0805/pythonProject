# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/2/25 20:43
# software: PyCharm
"""
文件说明：基本排序算法

"""


# 冒泡排序
def bubble_sort(arr):
    '''
    重复判断两个相邻元素是否符合要求，不符合就交换顺序；最多遍历n次
    注: 相邻元素相等时不会交换顺序，所以是稳定的
    :param arr:
    :return:
    '''
    n = len(arr)
    for i in range(n):  # 外循环
        flag = False  # 标志本轮是否交换过
        for j in range(0, n - i - 1):  # 内循环
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:  # 本轮没有进行交换，说明全部有序，退出循环
            return arr
    return arr


# 选择排序
def select_sort(arr):
    '''
    1. 在未排序的序列中找到最小(大)的元素, 存放到排序序列的起始位置
    2. 从剩余未排序的序列中继续寻找最小(大)的元素, 放到已经排序的序列末尾
    3. 重复 2 直到所有元素排序完毕
    注: 数组排序是不稳定的, 链表排序是稳定的
    :param arr:
    :return:
    '''
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


# 插入排序
def insert_sort(arr):
    '''
    1. 把待排序的数组分为已排序和未排序两部分, 初始时将第一个元素视为已排序
    2. 从第二个元素开始, 在已排序的子数组中找到适合的位置将当前数插入进去
    3. 重复步骤
    注: 稳定
    :param arr: 
    :return: 
    '''''
    for i in range(len(arr)):
        preIndex = i - 1
        current = arr[i]  # 当前待插入的数
        while preIndex >= 0 and arr[preIndex] > current:  # 当前数的前一位(有序数组的末尾) 大于当前值时
            arr[preIndex + 1] = arr[preIndex]  # 有序数组向后移动,腾出空间
            preIndex -= 1
        arr[preIndex + 1] = current  # 放置当前数
    return arr


# 快速排序
def quick_sort(arr):
    '''
    1. 从数组中跳出一个数作为基准 pivot
    2. 重新排列数列,所有比 pivot小的数放在 pivot前; 所有比 pivot大的数放在 pivot后面; 分区结束后pivot就在中间的位置
    3. 递归上述操作
    :param arr: 
    :return: 
    '''''
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[n // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


if __name__ == '__main__':
    arr = [1, 2, 3, 2, 5, 7, 5, 8, 88, 9, 3, 2]
    # print("冒泡排序：", bubble_sort(arr))
    # print("选择排序：", select_sort(arr))
    print("插入排序：", insert_sort(arr))
    print("快速排序：", quick_sort(arr))
