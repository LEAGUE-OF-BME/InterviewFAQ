# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSub(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 != None:
            if pRoot1.val != pRoot2.val:
                return False
            else:
                return self.isSub(pRoot1.left, pRoot2.left) and self.isSub(pRoot1.right, pRoot2.right)
        return False

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 == None:
            return False
        if pRoot1 == None:
            return False
        if self.isSub(pRoot1, pRoot2):
            return True
        else:
            return self.isSub(pRoot1.left, pRoot2) or self.isSub(pRoot1.right, pRoot2)
