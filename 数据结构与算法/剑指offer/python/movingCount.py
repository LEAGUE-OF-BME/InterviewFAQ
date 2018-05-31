# -*- coding:utf-8 -*-
class Solution:
    """
    地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
    但是不能进入行坐标和列坐标的数位之和大于k的格子。
    例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），
    因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
    """
    def movingCount(self, threshold, rows, cols):
        # write code here
        def neighbours(x, y):
            result = []
            if x > 0:
                result.append((x-1, y))
            if x < rows - 1:
                result.append((x+1, y))
            if y > 0:
                result.append((x, y-1))
            if y < cols - 1:
                result.append((x, y + 1))
            return result

        def isLegal(i, j):
            res = 0
            while i:
                res += i % 10
                i = i/10
            while j:
                res += j % 10
                j = j/10
            return res <= threshold

        def dfs(i, j, visited):
            if isLegal(i,j) and visited[i][j] == 0:
                visited[i][j] = 1
                for (x,y) in neighbours(i,j):
                    dfs(x,y, visited)

        visited = [[0]*cols for i in range(rows)]
        dfs(0,0,visited)
        ls = [sum(i) for i in visited]
        return sum(ls)
