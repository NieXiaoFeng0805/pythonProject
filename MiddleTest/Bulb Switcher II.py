# @Time: 2022/9/15 10:26
# @Author: 丨枫
# @File Bulb Switcher II.py
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        light_list = [1] * n
        print(light_list)
        # 经观察可知，灯泡状态以周期为6为一组，由此，可设置六个灯泡状态 6k+1，6k+2 ......
        # 再观察可得 6k+2和6k+6 的状态在不同开关控制下一致；6k+3和6k+5 的状态亦然
        # 进一步只用观察前四盏灯的状态即可 ； 设按下各个开关的次数 a,b,c,d
        #       ①6k+1的状态为(a + c + d) % 2
        #       ②6k+2的状态为(a + b) % 2
        #       ③6k+3的状态为(a + c) % 2
        #       ④6k+4的状态为(a + b + d) % 2
        # 由于①和③都受到1、3开关的影响，所以若①③状态相同，则d必然为偶数；若①③状态不同，则d必然为奇数
        # 由于②和④都受到1、2开关的影响，并且④和d有关系，所以若d为偶数，则②④状态相同；若d为奇数，则②④状态不同
        # 即可以通过①②③的状态来确定④的状态

        # 综上可得
        if presses == 0:
            return 1
        if n == 1:
            return 2
        elif n == 2:
            return 3 if presses == 1 else 4
        else:
            return 4 if presses == 1 else 7 if presses == 2 else 8


if __name__ == '__main__':
    Test = Solution()
    Test.flipLights(n=3, presses=1)
