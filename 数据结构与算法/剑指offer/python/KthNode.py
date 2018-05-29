# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        """
        给定一颗二叉搜索树，请找出其中的第k大的结点
        """
        # write code here
        ls = []
        def traversal(node):
            if node == None:
                return
            traversal(node.left)
            ls.append(node)
            traversal(node.right)

        traversal(pRoot)
        if k <= 0 or k > len(ls):
            return None
        else:
            return ls[k-1]
