# author: Feng
# contact: 1245272985@qq.com
# datetime:2022/10/11 8:57
# software: PyCharm
"""
文件说明：

"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0  # 记录有多少个字符不同，超过两个就说明不能一次转换
        n = len(s1)
        for i in range(n):
            # if s1[i] not in s2 or s2[i] not in s1:
            #     return False
            if s1[i] != s2[i]:
                if s1.count(s1[i]) != s2.count(s1[i]):
                    return False
                count += 1

        return True if count <= 2 else False


if __name__ == '__main__':
    Test = Solution()
    Test.areAlmostEqual(s1="attack", s2="defend")
