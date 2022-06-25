# @Time: 2022/4/26 9:15
# @Author: 丨枫
# @File 盛水最多的容器.py


class Solution(object):
    def maxArea(self, height):
        # # 暴力法
        # ArrList = []
        # MaxArea = []
        # # 寻找每个元素能取得的最大值即可
        # for i in range(len(height) - 1):
        #     for j in range(i + 1, len(height)):
        #         # 比大小选则高度
        #         if height[i] < height[j]:
        #             Areaheight = height[i]
        #         else:
        #             Areaheight = height[j]
        #         # 宽度
        #         AreaWidth = j - i
        #         # 面积
        #         Area = AreaWidth * Areaheight
        #         ArrList.append(Area)
        # MaxArea.append(max(ArrList))
        # # print(max(MaxArea))
        # return max(ArrList)

        # 双指针
        #左右指针
        left = 0
        right = len(height)-1
        MaxArea =0
        while left<right:
            #计算当前面积
            tempArea = min(height[left],height[right]) * (right-left)
            MaxArea=max(MaxArea,tempArea)#比较
            #移动短边指针
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        # print(MaxArea)
        return MaxArea
if __name__ == '__main__':
    Test = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Test.maxArea(height)
