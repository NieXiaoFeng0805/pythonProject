# @Time: 2022/7/11 10:23
# @Author: 丨枫
# @File RemoveKDigits.py
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        # 覆盖面太少
        """        
        # 拆分成列表
        num_list = [i for i in num]
        print(num_list)

        # 遍历
        minIndex = num_list.index(min(num_list))  # 最小值所在位置
        res = ''
        # print(minIndex)
        while k != 0:
            if minIndex > 0:  # 最小值不在第一个位置，将最小值前面的数删除
                num_list.pop(0)
                k -= 1
                minIndex = num_list.index(min(num_list))  # 更新位置
            if minIndex == 0:  # 最小值在第一个位置或次数用完
                res += num_list[minIndex]  # 添加到返回字符串中
                num_list.pop(minIndex)  # 删除原有的最小值
                minIndex = num_list.index(min(num_list))  # 更新位置
        res += ''.join(num_list)

        print(res)
        return res"""

        # 常规解法
        """     
        if len(num) == k:
            return "0" 
        # 尽量让较小的数靠前
        # 在第一个数确定时，若k>1，删除后面较大的数以让后面较小的数靠前；
        # 设置两个游标标识相邻两个数
        # 若 num_list[left]>num_list[right]  删除left对应元素 left = right ,right+=1
        left, right = 0, 1
        res = ''
        # 拆分成列表
        num_list = [i for i in num]
        # print(num_list)
        # print(''.join(num_list[:(len(num_list)-k)]))
        # 如果列表是按升序排列的，直接删除后面k个值即可

        if num_list == list(sorted(num_list)):
            return ''.join(num_list[:(len(num_list) - k)])
        while right < len(num_list):  # 遍历
            if num_list[left] > num_list[right]:  # 若高位大于低位则删除高位
                num_list.pop(left)
                k -= 1
                # 游标左移
                left -= 1
                right -= 1
                if left < 0:  # 若游标小于零则归零
                    left = 0
                    right = 1
                if k == 0:  # 若次数用尽则提前结束
                    break
                continue
            # 游标右移
            right += 1
            left += 1
        # 遍历结束但次数没有用完，删除其中的较大值
        if k != 0:
            for i in range(k):
                num_list.remove(max(num_list))
                # print(num_list)
        # 去除前导0
        for i in range(len(num_list)):
            if num_list[0] == '0':
                num_list.pop(0)
        # print(num_list)
        if len(''.join(num_list)) == 0:
            return '0'
        return ''.join(num_list)"""

        # 优化
        if len(num) == k:
            return "0"
        # 将删除k个值转换为保留len(num)-k个值
        stack = []
        remain = len(num) - k
        for i in num:
            while k and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        return ''.join(stack[:remain]).lstrip('0') or '0'


if __name__ == '__main__':
    Test = Solution()
    num, k = "996414363788153611534713021581934201828636847894114849949764848271145953346100425440564423705308160608336170309768131340987930561551032020085493444465193544083073070710550651127384420202284715693947961741503230801612259019643388373415242532432185095002546192236830917993656777205823895681565852256661971230933778711000024814024862198372554113821624993211934165249722752734719691558487424574765564337372811477100217812101347653217612856122765119173245525855698821566350946703626535675961447286537950070232309338175661044886376964501660879051008236994257987635984443260693570528423799185358552969157600544593174335218787781718110810765931666630909480297931136268524627123881164837747134261839114812308843935942493318281655037982696342444307736930338827080002496328501487998593220246931465776355431146576624189988605175259891929732507016317655984650530976168048173443438950167245619478608361175049157970111851326742552782365977460421387684737230598259483015657194376107329076625454990429534998668137411 ", 100
    Test.removeKdigits(num, k)
