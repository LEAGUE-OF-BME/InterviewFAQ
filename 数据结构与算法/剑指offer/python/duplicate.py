# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        dic = {}
        for i in numbers:
            if i in dic:
                duplication[0] = i
                return True
            else:
                dic[i] = 1
        return False
