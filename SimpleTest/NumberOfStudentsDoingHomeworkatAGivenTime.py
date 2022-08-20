# @Time: 2022/8/19 10:32
# @Author: 丨枫
# @File NumberOfStudentsDoingHomeworkatAGivenTime.py
class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        # 将两个列表整成一个字典
        # time_dict = dict(zip(startTime, endTime))
        # ans = 0
        # for s_time, e_time in time_dict.items():
        #     # 对字典遍历，只有q在中间的情况才能满情况
        #     if s_time <= queryTime and e_time >= queryTime:
        #         ans += 1
        # print(ans)
        # return ans
        n = len(startTime)
        ans = 0
        for s_time, e_time in zip(startTime, endTime):
            if s_time <= queryTime <= e_time:
                ans += 1
        print(ans)


if __name__ == '__main__':
    Test = Solution()
    Test.busyStudent(startTime=[19, 71, 9, 89, 57, 47, 57, 81], endTime=[93, 88, 23, 96, 82, 53, 91, 95], queryTime=63)
