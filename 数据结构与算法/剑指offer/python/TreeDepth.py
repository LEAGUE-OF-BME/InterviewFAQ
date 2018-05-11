# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return 1 + max(left, right)
