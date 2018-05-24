# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        ls = list(s)
        if len(s) == 0:
            return 0
        if ls[0] == '+' and len(ls) > 1:
            for i in ls[1:]:
                if i < '0' or i > '9':
                    return 0
            return int(''.join(ls[1:]))
        elif ls[0] == '-' and len(ls) > 1:
            for i in ls[1:]:
                if i < '0' or i > '9':
                    return 0
            return -int(''.join(ls[1:]))
        else:
            for i in ls:
                if i < '0' or i > '9':
                    return 0
            return int(''.join(ls))
