# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        val = pre[0]
        root = TreeNode(val)
        if len(pre) > 1:
            index = tin.index(val)
            left_tin = tin[:index]
            left_pre = pre[1:len(left_tin)+1]
            right_pre = pre[len(left_tin) + 1:]
            right_tin = tin[index+1:]
            root.left = self.reConstructBinaryTree(left_pre, left_tin)
            root.right = self.reConstructBinaryTree(right_pre, right_tin)
        return root
