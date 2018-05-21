# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        a1 = 0
        a2 = 0
        a3 = 0
        result = [1]
        for i in range(1, index):
            num = min([2*result[a1], 3*result[a2], 5*result[a3]])
            result.append(num)
            if num == 2*result[a1]:
                a1 += 1
            if num == 3*result[a2]:
                a2 += 1
            if num == 5*result[a3]:
                a3 += 1
        return result[-1]
