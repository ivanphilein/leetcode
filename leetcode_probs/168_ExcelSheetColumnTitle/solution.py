##Ideas:
# Tranfer a number from base 10 to base 26



class Solution:
    #def convertToTitle(self, n: int) -> str:
    def convertToTitle_v1(self, n: int):
        R = []
        while n > 0:
            m, n = (n-1) % 26, (n-1) // 26
            R.insert(0, chr(m + ord('A')))
            print(R)
            print(n)
            print("===")
        return "".join(R)

    def convertToTitle(self, n: int):
        R = []
        while n > 0:
            m = n % 26
            n = int(n/26)
            if m == 0:
                R.insert(0, chr(ord('Z')))
                n = n - 1
            else:
                R.insert(0, chr(m + ord('A') - 1))
        return "".join(R)




if __name__ == '__main__':
    n = 26 * 3
    sol = Solution()
    print(sol.convertToTitle_v1(n))
    print(sol.convertToTitle(n))
