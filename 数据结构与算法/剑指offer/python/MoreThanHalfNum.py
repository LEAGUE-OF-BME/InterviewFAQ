# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 0:
            return 0
        n = len(numbers) / 2
        for i in list(set(numbers)):
            if numbers.count(i) > n:
                return i
        return 0
