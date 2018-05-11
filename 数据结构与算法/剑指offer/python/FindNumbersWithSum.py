# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        dic = {}
        candidate = []
        for i in array:
            if tsum - i in dic:
                candidate.append(i)
            else:
                dic[i] = 1
        if len(candidate) == 0:
            return []
        candidate.sort(key=lambda x: x * (tsum-x))
        num1 = candidate[0]
        num2 = tsum - candidate[0]
        return min(num1, num2), max(num1, num2)
