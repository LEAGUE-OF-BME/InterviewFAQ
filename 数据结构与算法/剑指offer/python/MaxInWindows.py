# -*- coding:utf-8 -*-
class Solution:
    """
    给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
    例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
    """
    def maxInWindows(self, num, size):
        # write code here
        if size == 0 or size > len(num):
            return []

        result = []
        for i in range(len(num) - size + 1):
            result.append(max(num[i:i+size]))
        return result
