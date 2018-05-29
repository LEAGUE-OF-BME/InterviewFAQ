# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    """
    给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
    注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
    """
    def GetNext(self, pNode):
        # write code here
        def left_most(p):
            if p == None:
                return None
            while p.left:
                p = p.left
            return p

        if pNode == None:
            return None
        if pNode.right:
            return left_most(pNode.right)
        else:
            temp = pNode
            while temp.next:
                if temp.next.left == temp:
                    # pNode在某节点的左子树中
                    return temp.next
                temp = temp.next
            # 退到根节点
            return None
