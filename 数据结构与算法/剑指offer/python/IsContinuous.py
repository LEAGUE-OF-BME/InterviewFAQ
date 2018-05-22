# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) != 5:
            return False
        lo = 14
        hi = -1
        for i in numbers:
            if i!=0 and numbers.count(i) > 1:
                return False
            lo = i if i < lo and i > 0 else lo
            hi = i if i > hi else hi
        if hi - lo > 4:
            return False
        return True
