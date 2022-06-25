# @Time: 2022/5/20 18:21
# @Author: 丨枫
# @File RobotReturnToOrigin.py

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R'):
            return True
        else:
            return False


if __name__ == '__main__':
    Test = Solution()
    moves = "UR"
    Test.judgeCircle(moves)
