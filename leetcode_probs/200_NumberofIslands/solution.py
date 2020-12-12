##Ideas:
# Tranfer a number from base 10 to base 26



class Solution:
    #def numIslands(self, grid: List[List[str]]) -> int:
    def numIslands(self, grid):
        row_len = len(grid)
        col_len = len(grid[0])
        def valid(row_in, col_in):
            if row_in < 0 or row_in >=row_len or col_in<0 or col_in>=col_len:
                return False
            return True
        def search(seach_list):
            while(len(seach_list)>0):
                (r, c) = seach_list.pop(0)
                if valid(r-1, c) and grid[r-1][c] == "1":
                    grid[r-1][c] = "-1"
                    seach_list.append((r-1, c))
                if valid(r+1, c) and grid[r+1][c] == "1":
                    grid[r+1][c] = "-1"
                    seach_list.append((r+1, c))
                if valid(r, c-1) and grid[r][c-1] == "1":
                    grid[r][c-1] = "-1"
                    seach_list.append((r, c-1))
                if valid(r, c+1) and grid[r][c+1] == "1":
                    grid[r][c+1] = "-1"
                    seach_list.append((r, c+1))
        
        count = 0
        for r in range(row_len):
            row = grid[r]
            for c in range(col_len):
                num = int(row[c])
                if num <= 0:
                    continue
                if num == 1:
                    grid[r][c] = "-1"
                    count = count + 1
                    search([(r, c)])
        return count







if __name__ == '__main__':
    grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    sol = Solution()
    print(sol.numIslands(grid))