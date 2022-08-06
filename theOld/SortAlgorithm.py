# @Time: 2022/8/2 14:03
# @Author: 丨枫
# @File SortAlgorithm.py
import random


class Solution:
    def QuickSort(self, nums: list[int]) -> list[int]:  # 快速排序
        def partition(arr, low, high):
            pivot = arr[low]  # 选取最左边为pivot

            left, right = low, high  # 双指针
            while left < right:

                while left < right and arr[right] >= pivot:  # 找到右边第一个<pivot的元素
                    right -= 1
                arr[left] = arr[right]  # 并将其移动到left处

                while left < right and arr[left] <= pivot:  # 找到左边第一个>pivot的元素
                    left += 1
                arr[right] = arr[left]  # 并将其移动到right处

            arr[left] = pivot  # pivot放置到中间left=right处
            return left

        def randomPartition(arr, low, high):
            pivot_idx = random.randint(low, high)  # 随机选择pivot
            arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]  # pivot放置到最左边
            return partition(arr, low, high)  # 调用partition函数

        def quickSort(arr, low, high):
            if low >= high:  # 递归结束
                return
                # mid = partition(arr, low, high)       # 以mid为分割点【非随机选择pivot】
            mid = randomPartition(arr, low, high)  # 以mid为分割点【随机选择pivot】
            quickSort(arr, low, mid - 1)  # 递归对mid两侧元素进行排序
            quickSort(arr, mid + 1, high)

        quickSort(nums, 0, len(nums) - 1)  # 调用快排函数对nums进行排序
        return nums

    def MergeSort(self, nums: list[int], ) -> list[int]:  # 归并排序
        def mergeSort(arr, low, high):
            if low >= high:  # 递归结束标志
                return

            mid = low + (high - low) // 2  # 中间位置
            mergeSort(arr, low, mid)  # 递归对前后两部分进行排序
            mergeSort(arr, mid + 1, high)

            left, right = low, mid + 1  # 将arr一分为二：left指向前半部分（已有序），right指向后半部分（已有序）
            tmp = []  # 记录排序结果
            while left <= mid and right <= high:  # 比较排序，优先添加前后两部分中的较小者
                if arr[left] <= arr[right]:  # left指示的元素较小
                    tmp.append(arr[left])
                    left += 1
                else:  # right指示的元素较小
                    tmp.append(arr[right])
                    right += 1

            while left <= mid:  # 若左半部分还有剩余，将其直接添加到结果中
                tmp.append(arr[left])
                left += 1
            # tmp += arr[left:mid+1]        # 等价于以上三行

            while right <= high:  # 若右半部分还有剩余，将其直接添加到结果中
                tmp.append(arr[right])
                right += 1
            # tmp += arr[right:high+1]      # 等价于以上三行

            arr[low: high + 1] = tmp  # [low, high] 区间完成排序

        mergeSort(nums, 0, len(nums) - 1)  # 调用mergeSort函数完成排序
        return nums

    def StackSort(self, nums: list[int], ) -> list[int]:
        def maxHepify(arr, i, end):  # 大顶堆
            j = 2 * i + 1  # j为i的左子节点【建堆时下标0表示堆顶】
            while j <= end:  # 自上而下进行调整
                if j + 1 <= end and arr[j + 1] > arr[j]:  # i的左右子节点分别为j和j+1
                    j += 1  # 取两者之间的较大者

                if arr[i] < arr[j]:  # 若i指示的元素小于其子节点中的较大者
                    arr[i], arr[j] = arr[j], arr[i]  # 交换i和j的元素，并继续往下判断
                    i = j  # 往下走：i调整为其子节点j
                    j = 2 * i + 1  # j调整为i的左子节点
                else:  # 否则，结束调整
                    break

        n = len(nums)

        # 建堆【大顶堆】
        for i in range(n // 2 - 1, -1, -1):  # 从第一个非叶子节点n//2-1开始依次往上进行建堆的调整
            maxHepify(nums, i, n - 1)

        # 排序：依次将堆顶元素（当前最大值）放置到尾部，并调整堆
        for j in range(n - 1, -1, -1):
            nums[0], nums[j] = nums[j], nums[0]  # 堆顶元素（当前最大值）放置到尾部j
            maxHepify(nums, 0, j - 1)  # j-1变成尾部，并从堆顶0开始调整堆

        return nums


if __name__ == '__main__':
    Test = Solution()
    nums = [5, 1, 1, 2, 0, 0]
    Test.QuickSort(nums)
