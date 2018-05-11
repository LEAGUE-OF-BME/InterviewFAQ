# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, head):
        # write code here
        # a->b->c->None
        # None<-a<-b<-c
        pre = None
        while head != None:
            temp = head.next # 保存下一个节点
            head.next = pre # 反转
            pre = head # 向后移动
            head = temp # 向后移动
        return pre
