# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        ls = s.split(" ")
        if len(ls)<= 1:
            return s
        return " ".join(ls[::-1])
        
