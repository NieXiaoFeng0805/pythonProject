# @Time: 2022/7/13 15:08
# @Author: 丨枫
# @File HasCircleRoad.py
class Solution(object):
    def hasCycle(self, graph):
        """
        :type graph: str
        :rtype: bool
        """
        graph_split = graph.split(',')
        Pre_list = []
        Last_list = []
        for i in graph_split:
            temp = i.split('->')
            Pre_list.append(temp[0])
            Last_list.append(temp[1])

        print(Pre_list)
        print(Last_list)


if __name__ == '__main__':
    Test = Solution()
    graph = "1->4,2->5,3->6,3->7,4->8,5->8,5->9,6->9,6->11,7->11,8->12,9->12,9->13,10->13,10->14,11->10,11->14"
    Test.hasCycle(graph)
