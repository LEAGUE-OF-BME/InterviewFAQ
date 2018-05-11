# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        def reverse(matrix):
            """
            逆时针旋转
            """
            rev = []
            if len(matrix) == 0:
                return rev
            n = len(matrix[0])
            for i in range(n):
                rev.append([x[n-1-i] for x in matrix])
            return rev

        result = []
        while len(matrix) > 0:
            result.extend(matrix.pop(0))
            print(result)
            matrix = reverse(matrix)
        return matrix

if __name__ == '__main__':
    solution = Solution()
    solution.printMatrix([[1]])
