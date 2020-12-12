##Ideas:
# Every iteration, we consider the vaild subseuqnece which are ended with A[i]
# dp[i] 表示以 A[i] 为结尾的等差递增子区间的个数。
# 当 A[i] - A[i-1] == A[i-1] - A[i-2]，那么 [A[i-2], A[i-1], A[i]] 构成一个等差递增子区间。而且在以 A[i-1] 为结尾的递增子区间的后面再加上一个 A[i]，一样可以构成新的递增子区间。
#   dp[2] = 1
#   [0, 1, 2]
#   dp[3] = dp[2] + 1 = 2
#   [0, 1, 2, 3], // [0, 1, 2] 之后加一个 3
#   [1, 2, 3]     // 新的递增子区间
#   dp[4] = dp[3] + 1 = 3
#   [0, 1, 2, 3, 4], // [0, 1, 2, 3] 之后加一个 4
#   [1, 2, 3, 4],    // [1, 2, 3] 之后加一个 4
#   [2, 3, 4]        // 新的递增子区间
#综上，在 A[i] - A[i-1] == A[i-1] - A[i-2] 时，dp[i] = dp[i-1] + 1。


class Solution:
    #def numberOfArithmeticSlices(self, A: List[int]) -> int:
    def numberOfArithmeticSlices(self, A):
        if A is None:
            return 0
        a_len = len(A)
        if a_len < 3:
            return 0
        end = [0] * a_len
        for i in range(2, a_len):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                end[i] = end[i-1] + 1
        return sum(end)



if __name__ == '__main__':
    A = [0, 1, 2, 3, 4]
    sol = Solution()
    print(sol.numberOfArithmeticSlices(A))
