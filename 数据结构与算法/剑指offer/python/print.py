# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        """
        从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
        """
        # write code here
        if pRoot == None:
            return []
        queue = [pRoot]
        result = []
        while len(queue) > 0:
            n = len(queue)
            ls = []
            for i in range(n):
                node = queue.pop(0)
                ls.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(ls)
        return result
