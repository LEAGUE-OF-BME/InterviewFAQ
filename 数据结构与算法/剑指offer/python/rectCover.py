# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number < 1:
            return 0
        a = [0,1,2]
        for i in range(3, number+1):
            a.append(a[i-1] + a[i-2]) # 动态规划 第一块竖放：a[i-1]; 第一块横放：a[i-2]
        return a[number]
