# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/7 11:28
# software: PyCharm
"""
文件说明：四数之和

"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        if n < 4:
            return []
        res = []
        # 四个指针代表四位  ll,l,r,rr
        for ll in range(0, n - 4):
            if ll > 0 and nums[ll] == nums[ll - 1]: continue  # 保证ll发生了改变
            for l in range(ll + 1, n - 3):
                if l > ll + 1 and nums[l] == nums[l - 1]: continue  # 保证l发送改变
                r, rr = l + 1, n - 1
                while (r < rr):
                    if nums[ll] + nums[l] - target < -(
                            nums[r] + nums[rr]):  # 原写法num[a]+num[b]+num[c]+num[d]<target为了防止溢出,改一下
                        r += 1
                    elif nums[ll] + nums[l] - target > -(nums[r] + nums[rr]):  # 同上
                        rr -= 1
                    else:
                        res.append([nums[ll], nums[l], nums[r], nums[rr]])
                        while r < rr and nums[r + 1] == nums[r]:  # 保证r发送改变
                            r += 1
                        while r < rr and nums[rr - 1] == nums[rr]:  # 保证rr发送改变
                            rr -= 1
                        r += 1
                        rr -= 1
        return res
