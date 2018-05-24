# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = []
        forward = [1]
        backward = [1]
        n = len(A)
        for i in range(1,n):
            forward.append(forward[i-1] * A[i-1])
            backward.append(backward[i-1] * A[n-i])
        for i in range(n):
            B.append(forward[i]*backward[n-i-1])
        return B
