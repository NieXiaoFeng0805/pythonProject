# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/8 10:37
# software: PyCharm
"""
文件说明：

"""

'''
1. 数组长度确定
2. 对于数组内的选择，第一位肯定是1 (num_start=1)
3. 数字自增逻辑
    while(len(res_list)<n:   #当数组长度>=n时循环结束
        flag = False # 设置标识代表是否出现相加相等
        for i in res_list: # 对数组中的每个数都要遍历一次防止出现相加相等的情况
            若num_start + i < target: continue
            若num_start + i == target: flag=True
            若num_start + i > target: 直接添加target到数组中，此时还有两种情况
                若结果数组的长度刚好==n：直接返回数组和
                若结果数组长度<n: 添加target+1 target+2等到数组中
        if flag: 
            num_start+=1
            continue
    若遍历结束时,结果列表的末尾数小于target,则直接将其替换成target
            
'''

# 超时
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        res_list = [1]
        if n == 1:
            return target
        num_start = 2
        toCut = False
        res = 1
        while len(res_list) < n:  # 当数组长度>=n时循环结束
            flag = False  # 设置标识代表是否出现相加相等
            for i in res_list:  # 对数组中的每个数都要遍历一次防止出现相加相等的情况
                if num_start + i < target:
                    continue
                elif num_start + i == target:
                    flag = True
                    break
                else:
                    num_start = target if target != 1 else target + 1
                    toCut = True
                    break
            if flag:  # 出现相加相等
                num_start += 1
                continue
            else:
                res_list.append(num_start)
                res += num_start
                num_start += 1
            if toCut:  # 当出现了target后直接结束遍历,再后续中加入target+1 target+2即可
                break
        if len(res_list) < n:
            for i in range(n - len(res_list)):
                res_list.append(res_list[-1]+1)
        return sum(res_list) % (10**9+7)

#优化
'''
贪心,为了让数组之和最小，我们按照 1,2,3,⋯的顺序考虑,
但添加了 x之后，就不能添加 target−x; 因此最大可以添加到 target/2，
如果个数还不够 n 个，就继续从 target,target+1,target+2,依次添加。
'''
class Solution_1:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        mod = 10**9 + 7
        m = target // 2
        if n <= m:
            return ((1 + n) * n // 2) % mod
        return ((1 + m) * m // 2 + (target * 2 + (n - m) - 1) * (n - m) // 2) % mod

if __name__ == '__main__':
    S = Solution()
    S.minimumPossibleSum(n=11, target=1)
