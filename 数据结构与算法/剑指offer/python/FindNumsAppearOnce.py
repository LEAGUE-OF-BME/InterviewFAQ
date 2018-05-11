# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        dic = {}
        for i in array:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        result = []
        for i in array:
            if dic[i] == 1:
                result.append(i)
        return result
