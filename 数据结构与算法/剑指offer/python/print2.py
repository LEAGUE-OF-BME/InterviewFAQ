# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    """
    请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
    第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
    """
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        result = []
        queue = [pRoot]
        flag = False
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
            if flag:
                result.append(ls[::-1])
            else:
                result.append(ls)
            flag = not flag
        return result
