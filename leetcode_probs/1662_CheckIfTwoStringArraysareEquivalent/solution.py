##Ideas:
# Binary Search Tree, all nodes in the sub-left tree are smaller than the root and all nodes in the sub-right tree are larger than or equal to the root
# Solution: Divid and conquer
# Pick a value as root, then group all smller values as left tree and all larger or equal values are right tree, then build left and right tree


class Solution:
    #def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
    def arrayStringsAreEqual(self, word1, word2):
        cur_sec = word2.pop(0)
        cur_len = len(cur_sec)
        sec_in = 0
        empty_sec = False
        while(len(word1)>0):
            cur_fir = word1.pop(0)
            for c in cur_fir:
                if empty_sec is True:
                    return False
                if c != cur_sec[sec_in]:
                    return False
                sec_in = sec_in + 1
                if sec_in >= cur_len:
                    if len(word2) == 0:
                        empty_sec = True
                    else:
                        cur_sec = word2.pop(0)
                        cur_len = len(cur_sec)
                        sec_in = 0
        return True



if __name__ == "__main__":
    sol = Solution()
    word1 = ["a", "bc"]
    word2 = ["ab", "c"]
    print(sol.arrayStringsAreEqual(word1, word2))
