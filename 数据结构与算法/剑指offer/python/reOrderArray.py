# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        return [x for x in array if x % 2 != 0] + [x for x in array if x % 2 == 0]
