# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # https://www.nowcoder.com/practice/947f6eb80d944a84850b0538bf0ec3a5?tpId=13&tqId=11179&tPage=2&rp=2&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
    """
    输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
    """
    def process(self, root, ls):
        """
        中序遍历
        """
        if root == None:
            return
        self.process(root.left, ls)
        ls.append(root)
        self.process(root.right, ls)

    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
            return None
        ls = []
        self.process(pRootOfTree, ls)
        for i in range(len(ls)-1):
            node1 = ls[i]
            node2 = ls[i+1]
            node1.right = node2
            node2.left = node1
        return ls[0]
