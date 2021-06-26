class Solution:
    
    res = 0
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        startingPoint = self.findStartingPoint(grid)
        self.uniquePathsHelper(grid, startingPoint[0], startingPoint[1])
        return self.res        
        
    def uniquePathsHelper(self, grid, x, y):
        width, height = len(grid[0]), len(grid)
        if x < 0 or y < 0 or x >= width or y >= height or grid[y][x] == -1:
            return
        
        if grid[y][x] == 2:
            for i in range(height):
                for j in range(width):
                    if grid[i][j] == 0:
                        return
            self.res += 1
            return
        
        grid[y][x] = -1
        self.uniquePathsHelper(grid, x - 1, y)
        self.uniquePathsHelper(grid, x + 1, y)
        self.uniquePathsHelper(grid, x, y - 1)
        self.uniquePathsHelper(grid, x, y + 1)
        grid[y][x] = 0
        
        
        
    def findStartingPoint(self, grid):
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    return (x, y)

# ===============

