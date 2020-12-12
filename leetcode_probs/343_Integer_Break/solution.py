##Ideas:
# Loop from 1 to the given number n, for each number, find the biggest possible product output
# For number k, consider sum of (1, k-1), (2, k-2), ... until (m, k-m) when m>k-m, we can stop
# For each number, select the known biggest value, because for each m, and k-m, the possible biggest output is already known


class Solution:
    #def integerBreak(self, n: int) -> int:
    def integerBreak(self, n: int):
        if n < 2:
            return n
        prod = [1] * (n+1)
        for i in range(1, n+1):
            for j in range(1, i):
                if i-j < j:
                    break
                fir_v = max(prod[j], j)
                sec_v = max(prod[i-j], i-j)
                prod[i] = max(prod[i], fir_v*sec_v)
        return prod[n]



if __name__ == '__main__':
    n = 11
    sol = Solution()
    print(sol.integerBreak(n))
