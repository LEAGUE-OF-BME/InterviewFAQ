# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def length(self, root):
        if root == None:
            return 0
        left = self.length(root.left) + 1
        right = self.length(root.right) + 1
        return max(left, right)

    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        left = self.length(pRoot.left)
        right = self.length(pRoot.right)
        if left - right > 1 or left - right < -1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.left)
        
