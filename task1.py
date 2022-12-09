#Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

#Сложность данного алгоритма O(n)
#Сначала мы определяем координаты крайних ячеек матрицы и записываем их в стек
#Затем мы проходимся по матрице с координатами стека: если край, то его зануляем и соседей тоже (если единицы)
#После чего возвращаем сумму оставшихся единиц

def numEnclaves(grid):

    stack = {(0, 0)}
    for i in range(len(grid)):
        stack.add((i, 0))
        stack.add((i, len(grid[i])-1))
    for i in range(len(grid[0])):
        stack.add((len(grid)-1, i))
        stack.add((0, i))

    while stack:
        i, j = stack.pop()
        if grid[i][j] == 1:
            grid[i][j] = 0
            if len(grid) > i+1:
                stack.add((i+1, j))
            if len(grid[i]) > j+1:
                stack.add((i, j+1))
            if 0 <= i-1:
                stack.add((i-1, j))
            if 0 <= j-1:
                stack.add((i, j-1))
    s = 0
    for i in grid:
        s += sum(i)
    return s