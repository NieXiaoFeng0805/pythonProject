# @Time: 2022/9/5 14:10
# @Author: 丨枫
# @File Trapping Rain Water.py
# 求雨水(五种解法)
class Solution:
    def trap(self, height: list[int]) -> int:
        # 按行求
        n = len(height)
        if n < 3: return 0
        water = 0
        stack = []
        current_idx = 0

        while current_idx < n:
            # If stack is not empty and current height bigger than stack top's height
            while stack and height[current_idx] > height[stack[-1]]:
                h = height[stack.pop()]
                if not stack:
                    break
                # Distance between wall
                distance = current_idx - stack[-1] - 1
                min_height = min(height[stack[-1]], height[current_idx])
                water += distance * (min_height - h)

            stack.append(current_idx)
            current_idx += 1

        return water


# ##### Solution 5 --- DP and Two pointers O(n), O(1)
# 按列求
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         if n < 3: return 0
#         max_left = height[0]
#         max_right = height[-1]
#         water = 0

#         left, right = 1, n-2
#         for _ in range(1, n-1):
#             # Decide which side is shorter, calculate water and use
#             # max value of that side to update water.
#             if height[left-1] < height[right+1]:
#                 max_left = max(height[left-1], max_left)
#                 if max_left > height[left]:
#                     water += max_left - height[left]
#                 left += 1
#             else:
#                 max_right = max(height[right+1], max_right)
#                 if max_right > height[right]:
#                     water += max_right - height[right]
#                 right -= 1

#         return water

# ##### Solution 4 --- DP O(n), O(n)
# 动态规划
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         if n < 3: return 0
#         max_left = height[0]
#         max_right = [height[-1]]*n
#         water = 0

#         for i in range(n-2,-1,-1):
#             max_right[i] = max(max_right[i+1], height[i+1])

#         for i in range(1, n-1):
#             max_left = max(max_left, height[i-1])
#             h = min(max_left, max_right[i])
#             if h > height[i]:
#                 water += h-height[i]

#         return water

# ##### Solution 3 --- DP O(n), O(n)
# 双指针
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         if n < 3: return 0
#         max_left = [height[0]]*n
#         max_right = [height[-1]]*n
#         water = 0

#         for i in range(1, n):
#             max_left[i] = max(max_left[i-1], height[i-1])
#         for i in range(n-2,-1,-1):
#             max_right[i] = max(max_right[i+1], height[i+1])

#         for i in range(1, n-1):
#             h = min(max_left[i], max_right[i])
#             if h > height[i]:
#                 water += h-height[i]

#         return water

# ##### Solution 2 --- naive O(n^2), O(1)
# 栈
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         # Check for i-th column's left highest wall and right one,
#         # pick the short one and compare it with current height.
#         # If current is lower, add height difference to water, else,
#         # else there won't be any water.
#         n = len(height)
#         if n < 3: return 0

#         water = 0
#         h_left, h_right = height[0], height[-1]
#         # Skip first and last column, cuz there won't be water.
#         for i in range(1, n-1):
#             h_right = max(height[i+1:])
#             h = min(h_right, h_left)
#             if h > height[i]:
#                 water += h - height[i]
#             h_left = max(height[i], h_left)

#         return water

##### Solution 1  O(n), O(1)
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         ans = 0
#         h1 = 0
#         h2 = 0
#         for i in range(len(height)):
#             h1 = max(h1,height[i])
#             h2 = max(h2,height[-i-1])
#             ans += h1 + h2 -height[i]
#         return  ans - len(height)*h1
if __name__ == '__main__':
    Test = Solution()
    Test.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
