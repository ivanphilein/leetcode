##Ideas:
# Mentain two points, one from the beginning and one from the end
# If both two pointers are vowell letters, switch
# If left is not, move to right one step
# If right is not vowell, move to left one step

class Solution_v1:
    def reverseVowels(self, s: str) -> str:
        vowell_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        out_list = list()
        s_len = len(s)
        for i in range(s_len):
            out_list.append(s[i])
        left_p = 0
        right_p = len(s) - 1
        while(True):
            while(left_p < right_p and out_list[left_p] not in vowell_list):
                left_p = left_p + 1
            while(left_p < right_p and out_list[right_p] not in vowell_list):
                right_p = right_p - 1
            if left_p < right_p:
                temp = out_list[left_p]
                out_list[left_p] = out_list[right_p]
                out_list[right_p] = temp
                left_p = left_p + 1
                right_p = right_p - 1
            else:
                break
        return ''.join(out_list)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowell_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        out_list = [None] * len(s)
        left_p = 0
        right_p = len(s) - 1
        while(left_p <= right_p):
            left_item = s[left_p]
            right_item = s[right_p]
            if s[left_p] not in vowell_list:
                out_list[left_p] = left_item
                left_p = left_p + 1
            elif right_item not in vowell_list:
                out_list[right_p] = right_item
                right_p = right_p - 1
            else:
                out_list[right_p] = left_item
                out_list[left_p] = right_item
                left_p = left_p + 1
                right_p = right_p - 1
        return ''.join(out_list)




if __name__ == '__main__':
    s = "hello"
    s = "leetcode"
    sol = Solution()
    print(sol.reverseVowels(s))



