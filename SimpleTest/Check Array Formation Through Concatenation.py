# @Time: 2022/9/23 17:49
# @Author: 丨枫
# @File Check Array Formation Through Concatenation.py
class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        """
        if len(pieces) == 1:
            return arr == pieces[0]
        for i in arr:
            flag = False
            for j in pieces:
                j_len = len(j)
                if i not in j:  # 不在这里面
                    flag = True
                    continue
                elif i in j and j_len == 1:  # 存在
                    flag = False
                    j.pop()
                    break
                if j_len > 1 and j[0] != i:  # 位置不对，不管怎么移动都不能和原来一样
                    return False
                elif j_len > 1 and j[0] == i:  # 将等于的位置上的元素弹出
                    flag = False
                    j.pop(0)
                    break  # 进入下一个值的确定
            if flag:  # pieces里面没有这个数
                return False
        return True"""

        n, m = len(arr), len(pieces)
        hash = [0] * 110
        for i in range(m):
            hash[pieces[i][0]] = i
        i = 0
        while i < n:
            cur = pieces[hash[arr[i]]]
            sz, idx = len(cur), 0
            while idx < sz and cur[idx] == arr[i + idx]:
                idx += 1
            if idx == sz:
                i += sz
            else:
                return False
        return True

if __name__ == '__main__':
    Test = Solution()
    # Test.canFormArray(arr=[100, 2, 98, 28, 44, 55, 37], pieces=[[28, 46, 57], [37, 19, 40, 38]])
    Test.canFormArray(arr=[1, 2, 3], pieces=[[2], [1, 3]])
