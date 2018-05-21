# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 == None or pHead2 == None:
            return None
        p1 = pHead1
        p2 = pHead2
        a = 1
        b = 1
        while p1 and p1.next:
            a += 1
            p1 = p1.next
        while p2 and p2.next:
            p2 = p2.next
            b += 1
        if p1 != p2:
            return None
        if a > b:
            p1,p2 = pHead1,pHead2
        else:
            p1,p2 = pHead2, pHead1
        for i in range(abs(a-b)):
            p1 = p1.next
        while p1!=p2:
            p1 = p1.next
            p2 = p2.next
        return p1
