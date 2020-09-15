##Ideas:
# Idea: 
# 1: have a sub-function to check whether a string is a subsequence of the target string
# 2: Maintan a best fit string so far
# 3: For each given string, compare it to the best solution. If len(string) < len(best) or len(string) == len(best) but not < in lexicographical order, ignore
# 4: else: check whether this string is a possible solution or not, if yes, update the best solutions

# Double pointers used to check whether one string is a sub-sequence of the other string

class Solution:
    # Check whether sub is a subsequence of sup
    def is_substr(self, sup, sub):
        s_iter = 0
        t_iter = 0
        while(s_iter < len(sup) and t_iter < len(sub)):
            if sup[s_iter] == sub[t_iter]:
                t_iter = t_iter + 1
            s_iter = s_iter + 1
        return t_iter == len(sub)

    def findLongestWord(self, sup: str, d: List[str]) -> str:
        best_sofar = ""
        for sub in d:
            if len(sub)<len(best_sofar) or (len(sub)==len(best_sofar) and best_sofar < sub):
                continue
            if self.is_substr(sup, sub) is True:
                best_sofar = sub
        return best_sofar


