##Ideas:
# Search over the first column first, then the first row



class Solution:
    #def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    def searchMatrix(self, matrix, target: int):
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        # end = n and not valid
        def searchCol(start, end):
            if start < 0 or start>=m:
                return -1
            if start >= end-1:
                return start
            if matrix[start][0]>target:
                return -1
            middle = (end-start)//2 + start
            if matrix[middle][0] == target:
                return middle
            elif matrix[middle][0]<target:
                return searchCol(middle, end)
            else:
                return searchCol(start, middle)

        col_index = searchCol(0, m)
        if col_index < 0:
            return False
        def searchRow(start, end, row=0):
            if start < 0 or start>=n:
                return False
            if start >= end-1:
                return (matrix[row][start] == target)
            middle = (end-start)//2 + start
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle]<target:
                return searchRow(middle+1, end, row)
            else:
                return searchRow(start, middle, row)
        return searchRow(0, n, col_index)

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 3
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 13
    matrix = []
    target = 0
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 10
    matrix = [[1,1]]
    target = 2
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 11
    sol = Solution()
    print(sol.searchMatrix(matrix, target))
