import numpy as np
class Solution(object):
    matrix = None
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s = len(s)
        len_p = len(p)
        if self.matrix is None:
            while "**" in p:
                p = p.replace("**", "*")
            self.matrix = np.zeros((len_s + 1, len_p + 1))
            self.matrix = self.matrix - 1

        if p=='*':
            self.matrix[len_s, len_p] = 1
            return True
        if '*' not in p:
            if len(s) != len(p):
                self.matrix[len_s, len_p] = 0
                return False
        if len(s) == 0:
            if len(p) == 0:
                self.matrix[len_s, len_p] = 1
                return True
            else:
                self.matrix[len_s, len_p] = 0
                return False

        if len(p) == 0:
            self.matrix[len_s, len_p] = 0
            return False

        if self.matrix[len_s, len_p] == 1:
            return True
        elif self.matrix[len_s, len_p] == 0:
            return False
        
        # if len(s) == 1:
        #     p = p.replace('*', '')
        #     if p == "" or p == '?':
        #         self.matrix[len_s, len_p] = 1
        #         return True
        #     if s == p:
        #         self.matrix[len_s, len_p] = 1
        #         return True
        #     else:
        #         self.matrix[len_s, len_p] = 0
        #         return False
        # else:
        #     if len(p) == 1:
        #         self.matrix[len_s, len_p] = 0
        #         return False

        if p[0] == '*':
            ret_bool = (self.isMatch(s[1:], p[1:]) or self.isMatch(s[1:], p) or self.isMatch(s, p[1:]))
            if ret_bool is True:
                self.matrix[len_s, len_p] = 1
            else:
                self.matrix[len_s, len_p] = 0
            return ret_bool
        elif s[0] == p[0] or p[0]=='?':
            ret_bool = self.isMatch(s[1:], p[1:])
            if ret_bool is True:
                self.matrix[len_s, len_p] = 1
            else:
                self.matrix[len_s, len_p] = 0
            return ret_bool
        self.matrix[len_s, len_p] = 0
        return False

# class Solution(object):
#     def isMatch(self, s, p, matrix=None):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         i = 0
#         j = 0
#         iStar = -1
#         jStar = -1
#         while("**" in p):
#             p = p.replace('**', '*')
        
#         if p == '*':
#             return True
#         if len(s) == 0:
#             if len(p) > 0:
#                 return False
#         elif len(p) == 0:
#             return False

#         while(i < len(s) and j < len(p)):
#             if s[i] == p[j] or p[j] == '?':
#                 i = i + 1
#                 j = j + 1
#             elif p[j] == '*':
#                 iStar = i
#                 jStar = j
#                 j = j + 1
#             elif iStar > 0:
#                 i = i + 1
#             else:
#                 return False
#         if j < len(p):
#             while (p[j] == '*'):
#                 j = j +1
#         return j == len(p)


if __name__ == "__main__":
    s = "ho"
    p = "ho****"
    #s = "a"
    #p = "****a***"
    #s = "abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb"
    #p = "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**"
    #s = "mississippi"
    #p = "m??*ss*?i*pi"
    #s = "zacabz"
    #p = "*a?b*"
    #s = "z"
    #p = "b*"
    #s = "bbbaaabaababbabbbaabababbbabababaabbaababbbabbbabb"
    #p = "*b**b***baba***aaa*b***"
    #s = "aa"
    #p = "a****"
    #s = "bbbbbbbabbaabbabbbbaaabbabbabaaabbababbbabbbabaaabaab"
    #p = "b*b*ab**ba*b**b***bba"
    
    ob = Solution()
    print ob.isMatch(s, p)
    