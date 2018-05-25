# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    """
    请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
    """
    def isSymmetrical(self, pRoot):
        # write code here
        def isSame(p1, p2):
            """
            比较两个节点是否相同
            """
            if p1==None and p2==None:
                return True
            if p1 and p2 and p1.val == p2.val:
                return True
            else:
                return False

        if pRoot == None:
            return True
        left = [pRoot.left] # 从左到右的顺序
        right = [pRoot.right] # 从右到左的顺序
        while len(left)>0:
            pLeft = left.pop(0)
            pRight = right.pop(0)
            if not isSame(pLeft, pRight):
                return False
            else:
                if pLeft: # pLeft非空，pRight必定非空，否则比较的时候已经返回False
                    left.append(pLeft.left)
                    left.append(pLeft.right)
                    right.append(pRight.right)
                    right.append(pRight.left)
        return True
