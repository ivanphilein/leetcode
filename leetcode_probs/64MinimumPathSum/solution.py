##Ideas:
# At each point, the point can either go down or go right
# S_{i, j} = Min(S_{i-1, j}, S_{i, j-1}) + V_{i, j}
import numpy as np

class Solution_1:
    #def minPathSum(self, grid: List[List[int]]) -> int:
    def minPathSum(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        s_matrix = np.zeros((m, n))
        s_matrix[0, 0] = grid[0][0]
        for i in range(0, m):
            grid_row = grid[i]
            for j in range(0, n):
                from_his = -1
                if i > 0:
                    from_his = s_matrix[i-1, j]
                if j > 0:
                    if from_his == -1:
                        from_his = s_matrix[i, j-1]
                    else:
                        from_his = min(from_his, s_matrix[i, j-1])
                if from_his == -1:
                    continue
                s_matrix[i, j] = from_his + grid_row[j]
        return s_matrix[m-1, n-1]

class Solution:
    #def minPathSum(self, grid: List[List[int]]) -> int:
    def minPathSum(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        s_row = [0] * n
        for i in range(0, m):
            grid_row = grid[i]
            for j in range(0, n):
                if j == 0:
                    s_row[j] = s_row[j]
                elif i == 0:
                    s_row[j] = s_row[j-1]
                else:
                    s_row[j] = min(s_row[j], s_row[j-1])
                s_row[j] = s_row[j] + grid_row[j]
        return int(s_row[n-1])


if __name__ == "__main__":
    grid = [[1,3,1], [1,5,1], [4,2,1]]
    sol = Solution()
    print(sol.minPathSum(grid))
