##Ideas:
# Tranfer a number from base 10 to base 26



class Solution:
    #def titleToNumber(self, s: str) -> int:
    def titleToNumber(self, s: str):
        ret_num = 0
        for c in s:
            num = ord(c) - 65 + 1
            ret_num = ret_num * 26 + num
        return ret_num



if __name__ == '__main__':
    n = "Z"
    sol = Solution()
    print(sol.titleToNumber(n))