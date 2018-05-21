# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        ls = list(s)
        length = len(ls)
        if length == 0:
            return s
        num = n % length
        return ''.join(ls[num:] + ls[:num])
