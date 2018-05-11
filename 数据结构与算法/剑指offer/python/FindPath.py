# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.result = []
        self.path = []

    def FindPath(self, root, expectNumber):
        # write code here
        if root == None:
            return []
        self.path.append(root)
        if root.val == expectNumber and root.left == None and root.right == None:
            self.result.append([node.val for node in self.path])
        else:
            self.FindPath(root.left, expectNumber - root.val)
            self.FindPath(root.right, expectNumber - root.val)
        self.path.pop()

        return self.result
