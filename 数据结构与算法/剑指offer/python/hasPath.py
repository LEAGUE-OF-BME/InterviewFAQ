# -*- coding:utf-8 -*-
class Solution:
    """
    请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
    路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
    如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
    例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，
    但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
    """
    def __init__(self):
        self.flag = False
    def hasPath(self, matrix, rows, cols, path):

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

        def dfs(i, j, visited, ls, path):
            if visited[i][j] == 0:
                ls.append(matrix[i][j])
                visited[i][j] = 1
                if ls == path:
                    self.flag = True
                if len(ls) < len(path) and ls == path[:len(ls)]:
                    for (x, y) in neighbours(i,j):
                        dfs(x, y, visited, ls, path)
                ls.pop()
                visited[i][j] = 0


        path = list(path)
        if rows == 0 or cols == 0:
            return False
        matrix = [matrix[i*cols:i*cols+cols] for i in range(rows)]
        print(matrix)
        visited = [[0]*cols for k in range(rows)]
        ls = []
        for i in range(rows):
            for j in range(cols):
                visited = [[0]*cols for k in range(rows)]
                ls = []
                flag = False
                dfs(i,j, visited, ls, path)
                if self.flag:
                    return True
        return False
