# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        for i in range(1, len(rotateArray)):
            if i + 1 < len(rotateArray) and rotateArray[i] > rotateArray[i+1]:
                return rotateArray[i+1]
        return rotateArray[0]
