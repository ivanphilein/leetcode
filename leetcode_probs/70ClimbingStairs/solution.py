##Ideas:
# For the nth step, the ways to get the nth step are decided by the ways the get the n-1 step and n-2 step.
# dp[n] = dp[n-1] + dp[n-2]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:  ## Alwasy starts with the simplest cases
            return n

        s_n = 0
        s_pre2 = 1
        s_pre1 = 2
        for i in range(2, n):
            s_n = s_pre1 + s_pre2
            s_pre2 = s_pre1
            s_pre1 = s_n
        return s_n

if __name__ == "__main__":
    n = 4
    sol = Solution()
    print(sol.climbStairs(n))
