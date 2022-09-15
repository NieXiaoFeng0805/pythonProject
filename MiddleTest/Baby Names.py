# @Time: 2022/9/6 13:53
# @Author: 丨枫
# @File Baby Names.py
import re


class Solution:
    def trulyMostPopular(self, names: list[str], synonyms: list[str]) -> list[str]:
        # 将姓名和次数作为字典
        for i in names:
            nums = ''.join(re.findall(r"\d+", i))
            print(nums)
        nums_dict = {}
        # 将重复姓名进行整合


if __name__ == '__main__':
    Test = Solution()
    Test.trulyMostPopular(names=["John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"],
                          synonyms=["(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"])
