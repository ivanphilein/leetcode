##Ideas:
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# Given one target number, t, loop i from 1 to t, the least of t is equal to the sum of least of (t-i*i) and 1, here 1 because i*i is a perfect sequare.
# Repeat the previous operation until the input n
#
#
# Assume least[n] is the least number of perfect square numbers with sum to n
# Loop from 1 to n, find the corresponding perfect square numbers. In first iteration, the per is 1, in the second iteration the per is 4
# Each iteration, least[n] = min(least[n], 1+least[n-per]). Now, we need to loop from 1 to n, to get all least values for numbers 1 to n
# Loop i from 1 to n, second loop j from 1 to n as well, j2 = j * j, if j2 > i, break, then least[i] = min(least[i], 1+least[i-j2])

class Solution:
    #def numSquares(self, n: int) -> int:
    def numSquares(self, n: int):
        least = list(range(n+1))
        for i in range(1, n+1):
            for j in range(1, i):
                j2 = j * j
                if j2 > i:
                    break
                least[i] = min(least[i], 1+least[i-j2])
        return least[n]




if __name__ == '__main__':
    n = 13
    sol = Solution()
    print(sol.numSquares(n))
