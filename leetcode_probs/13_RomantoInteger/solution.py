##Ideas:
# Given Raman number and convert it into integer.
# If a letter is smaller than the next letter, it is sub, otherwise, add


class Solution:
    #def romanToInt(self, s: str) -> int:
    def romanToInt(self, s: str):
        symbol_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ret_v = 0
        pre_v = -1
        for c in s:
            c_val = symbol_dict[c]
            if pre_v>=0 and c_val > pre_v:
                ret_v = ret_v - pre_v + c_val - pre_v
                pre_v = -1
            else:
                ret_v = ret_v + c_val
                pre_v = c_val
        return ret_v




if __name__ == "__main__":
    sol = Solution()
    s = "IV"
    s = "IX"
    s = "LVIII"
    s = "MCMXCIV"
    print(sol.romanToInt(s))
