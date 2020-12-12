##Ideas:
# Solution 1: 
# Solution: Divid and conquer
# Pick a value as root, then group all smller values as left tree and all larger or equal values are right tree, then build left and right tree


class Solution:
    #def longestCommonPrefix(self, strs: List[str]) -> str:
    def longestCommonPrefix(self, strs):
        len_strs = len(strs)
        if len_strs == 0:
            return ""
        if len_strs == 1:
            return strs[0]
        fir_str = strs[0]
        sec_index = 1
        while(sec_index < len_strs and len(fir_str)>0):
            sec_str = strs[sec_index]
            fir_str = self.lcp_two(fir_str, sec_str)
            sec_index = sec_index + 1
        return fir_str


    def lcp_two(self, fir_str, sec_str):
        fir_len = len(fir_str)
        sec_len = len(sec_str)
        pointer = 0
        while(pointer < fir_len and pointer < sec_len):
            if fir_str[pointer] == sec_str[pointer]:
                pointer = pointer + 1
            else:
                break
        if pointer == 0:
            return ""
        else:
            return fir_str[0:pointer]



if __name__ == "__main__":
    sol = Solution()
    strs = ["flower","flow","flight"]
    strs = ["dog","racecar","car"]
    #print(sol.lcp_two(strs[0], strs[2]))
    print(sol.longestCommonPrefix(strs))
