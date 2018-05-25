# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        """
        在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
        例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
        """
        # write code here
        if pHead == None:
            return None
        if not pHead.next:
            return pHead
        temp = pHead.next
        if pHead.val == temp.val: # 头指针重复，找到第一个不重复的节点，递归
            while temp and temp.val == pHead.val:
                temp = temp.next
            return self.deleteDuplication(temp)
        else: # 头指针不重复，直接递归下一个节点
            pHead.next = self.deleteDuplication(pHead.next)
            return pHead
