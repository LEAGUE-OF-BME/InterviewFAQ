# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        root = sequence[-1]
        left = []
        right = []
        for i, x in enumerate(sequence):
            if x > root:
                left = sequence[:i]
                right = sequence[i: len(sequence)-1]
                break
        for x in right:
            if x < root:
                return False
        l = True if len(left) == 0 else self.VerifySquenceOfBST(left)
        r = True if len(right) == 0 else self.VerifySquenceOfBST(right)
        return l and r 
