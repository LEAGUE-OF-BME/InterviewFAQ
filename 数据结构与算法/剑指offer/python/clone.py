# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # https://www.nowcoder.com/practice/f836b2c43afc4b35ad6adc41ec941dba?tpId=13&tqId=11178&tPage=2&rp=2&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead == None:
            return None
        origin = pHead
        origin_nodes = [pHead]
        new_head = RandomListNode(pHead.label)
        new_nodes = [new_head]
        temp = new_head
        while pHead.next:
            pHead = pHead.next
            origin_nodes.append(pHead)
            node = RandomListNode(pHead.label)
            new_nodes.append(node)
            temp.next = node
            temp = temp.next

        pHead = origin
        temp = new_head
        while pHead:
            random = pHead.random
            if random == None:
                temp.random = None
            else:
                temp.random = new_nodes[origin_nodes.index(random)]
            pHead = pHead.next
            temp = temp.next

        return new_head
