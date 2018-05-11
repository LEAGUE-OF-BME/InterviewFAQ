# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root == None:
            return []
        result = []
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            result.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return result
