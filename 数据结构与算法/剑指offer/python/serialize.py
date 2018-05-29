# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    """
    请实现两个函数，分别用来序列化和反序列化二叉树
    """
    def Serialize(self, root):
        # write code here
        ls = []
        def process(root):
            if root == None:
                ls.append("$")
                return
            ls.append(str(root.val))
            process(root.left)
            process(root.right)
        process(root)
        return ','.join(ls)

    def Deserialize(self, s):
        # write code here
        ls = s.split(',')
        def process():
            val = ls.pop(0)
            if val == "$":
                return None
            node = TreeNode(int(val))
            node.left = process()
            node.right = process()
            return node

        return process()
