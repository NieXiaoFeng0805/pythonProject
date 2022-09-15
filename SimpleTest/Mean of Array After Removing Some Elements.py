# @Time: 2022/9/14 15:29
# @Author: 丨枫
# @File Mean of Array After Removing Some Elements.py
from numpy import mean


class Solution:
    def trimMean(self, arr: list[int]) -> float:
        n = len(arr)
        arr.sort()
        print(arr)
        fd, ld = n * 0.05, n * 0.05
        print(fd, ld)
        new_arr = arr[int(fd):(n-int(ld))]
        print(mean(new_arr))
        return mean(new_arr)


if __name__ == '__main__':
    Test = Solution()
    Test.trimMean(arr=[6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4])
