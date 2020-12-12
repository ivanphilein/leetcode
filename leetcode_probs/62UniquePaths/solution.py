##Ideas:
# At each point, the point can either go down or go right
# S_{i, j} = S_{i-1, j} + S{i, j-1}



class Solution:
    #def uniquePaths(self, m: int, n: int) -> int:
    def uniquePaths(self, m: int, n: int):
        if m==0 or n==0:
            return 0
        all_path = 0
        path_row = [1] * n
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    path_row[j] = path_row[j]
                else:
                    path_row[j] = path_row[j] + path_row[j-1]
        return path_row[-1]



if __name__ == "__main__":
    m = 3
    n = 3
    sol = Solution()
    print(sol.uniquePaths(m, n))
