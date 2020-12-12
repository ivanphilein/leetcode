##Ideas:
# Loop from the first digital letter to the last digital letter
# code list from 0 to len(s)
# code[0] = 0
# in each iteration i, consider s[i] and s[i-1], if s[i-1]*10+s[i]<=26, it means s[i-1]s[i] can be either considered as one letter or sperate to be two
# In this case, code[i] = code[i-1] + code[i-2], here code[i-1] means seperate i-1 and i, code[i-2] means combine i-1 and i together
# Else, s[i-1]*10+s[i]>26, it means s[i-1] and s[i] have to be seperated, in this case, code[i] = code[i-1]



class Solution:
    #def numDecodings(self, s: str) -> int:
    def numDecodings(self, s: str):
        if s is None or s.startswith('0'):
            return 0
        s_len = len(s)
        code = [0] * (s_len + 1)
        code[1] = 1
        for i in range(2, s_len+1):
            int_v = int(s[i-2:i])
            if int_v == 0:
                return 0
            if s[i-1] == '0':
                if int_v > 26:
                    return 0
                else:
                    code[i] = code[i-1] - code[i-2]
            elif s[i-2] == '0':
                code[i] = code[i-1]
            else:
                if int(s[i-2:i]) > 26:
                    code[i] = code[i-1]
                else:
                    code[i] = code[i-2] + code[i-1]
        return code[s_len]
        #return code




if __name__ == '__main__':
    s = "226"
    s = "12345123"
    s = "10"
    s = "2101"
    sol = Solution()
    print(sol.numDecodings(s))
