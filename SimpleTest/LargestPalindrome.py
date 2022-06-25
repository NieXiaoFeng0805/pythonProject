# @Time: 2022/6/24 13:14
# @Author: 丨枫
# @File LargestPalindrome.py
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 能构建的回文串有两则形式
        # 一是全部都是成对出现的；二是有一个字母是奇数个，其余都是成对出现的
        # 计算字符串中相同字母出现的个数，若是偶数倍则必然可以成，若有奇数字符出现且数量不等于1则加上数量-1即可；
        # 返回计数器
        rs = s[::-1]
        if rs == s:
            return len(s)
        alphatable = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']
        counter = 0  # 偶、奇
        flag = False
        for i in alphatable:
            num = s.count(i)  # 计算个数
            num1 = s.count(i.upper())
            if num % 2 == 0:  # 偶数个
                counter += num
            if num % 2 != 0:  # 大于1的奇数个
                flag = True
                counter += num - 1
            if num1 % 2 == 0:  # 大写偶数个
                counter += num1
            if num1 % 2 != 0:  # 大写奇数个
                flag = True
                counter += num1 - 1

        if flag:
            return counter + 1
        else:
            return counter


if __name__ == '__main__':
    Test = Solution()
    s = "jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"
    Test.longestPalindrome(s)
