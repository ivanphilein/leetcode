##Ideas:
# BFS search, from each node i, search all connected nodes (up to 8), and update their costs to be min(current_cost, cost_i+1)


class Solution:
    #def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    def shortestPathBinaryMatrix(self, grid):
        #1 <= grid.length == grid[0].length <= 100
        row_len = len(grid)
        col_len = len(grid[0])
        if grid[0][0] != 0:
            return -1
        if grid[row_len-1][col_len-1] != 0:
            return -1
        cost_grid = x = [[-1]*col_len for i in range(row_len)]
        cost_grid[0][0] = 1
        visit_list = [(0, 0)]

        def cost_update(next_row, next_col, next_cost):
            if next_row < 0 or next_col < 0:
                return False
            if next_row >=row_len or next_col >= col_len:
                return False
            if grid[next_row][next_col] != 0:
                return False
            if cost_grid[next_row][next_col] < 0:
                cost_grid[next_row][next_col] = next_cost
                return True
            elif cost_grid[next_row][next_col] > next_cost:
                cost_grid[next_row][next_col] = next_cost
                return True

        while(len(visit_list)>0):
            node = visit_list.pop(0)
            row_in = node[0]
            col_in = node[1]
            node_cost = cost_grid[row_in][col_in]
            if node_cost < 0:
                continue

            if (cost_update(row_in+1, col_in, node_cost+1)):
                visit_list.append((row_in+1, col_in))
            if (cost_update(row_in+1, col_in+1, node_cost+1)):
                visit_list.append((row_in+1, col_in+1))
            if (cost_update(row_in+1, col_in-1, node_cost+1)):
                visit_list.append((row_in+1, col_in-1))
            if (cost_update(row_in-1, col_in, node_cost+1)):
                visit_list.append((row_in-1, col_in))
            if (cost_update(row_in-1, col_in-1, node_cost+1)):
                visit_list.append((row_in-1, col_in-1))
            if (cost_update(row_in-1, col_in+1, node_cost+1)):
                visit_list.append((row_in-1, col_in+1))
            if (cost_update(row_in, col_in+1, node_cost+1)):
                visit_list.append((row_in, col_in+1))
            if (cost_update(row_in, col_in-1, node_cost+1)):
                visit_list.append((row_in, col_in-1))

        return cost_grid[row_len-1][col_len-1]

if __name__ == "__main__":
    sol = Solution()
    grid = [[0, 0, 0], [1, 1, 1], [1, 1, 0]]
    #grid = [[0,1],[1,0]]
    grid = [[0,0,1,0,0,0,0],[0,1,0,0,0,0,1],[0,0,1,0,1,0,0],[0,0,0,1,1,1,0],[1,0,0,1,1,0,0],[1,1,1,1,1,0,1],[0,0,1,0,0,0,0]]
    print(sol.shortestPathBinaryMatrix(grid))
