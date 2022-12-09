#Сложность алгоритма O(n*m)
#реализуется с помощью обхода в глубину
#все острова по краю матрицы превращаются в воду
#затем выполняется поиск в глубину по оставшимся островам и находится их сумма

def closedIsland(grid):
    m, n = len(grid), len(grid[0])
    def dfs(i, j):
        if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
            grid[i][j] = 1
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
    
    
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                dfs(i, j)
                
    islands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                dfs(i, j)
                islands += 1
    return islands