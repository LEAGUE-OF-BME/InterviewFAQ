# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        while len(popV) > 0:
            n = popV.pop(0)
            if n not in pushV:
                return False
            index = pushV.index(n)
            if index > 0 and popV[0] in pushV[:index-1]:
                return False
            else:
                pushV.pop(index)
        return True
