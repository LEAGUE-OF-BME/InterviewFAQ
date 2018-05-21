# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        ls = list(s)
        dic = {}
        for i in ls:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in ls:
            if i in dic and dic[i] == 1:
                return ls.index(i)
        return -1
