##Ideas:
# Sol1: Convert the int to string, and use two pointer to check
# Time: O(n), Space: O(1)
# 


class Solution:
    #def isPalindrome(self, x: int) -> bool:
    def isPalindrome_v1(self, x: int):
        x_str = str(x)
        x_len = len(x_str)
        fir_p = 0
        sec_p = x_len-1
        while(fir_p<sec_p):
            if x_str[fir_p] != x_str[sec_p]:
                return False
            fir_p = fir_p + 1
            sec_p = sec_p - 1
        return True

    def isPalindrome_v2(self, x: int):
        if x < 0:
            return False
        digit_list = []
        while(x>0):
            digit_list.append(x%10)
            x = x // 10
        fir_p = 0
        sec_p = len(digit_list)-1
        while(fir_p<sec_p):
            if digit_list[fir_p] != digit_list[sec_p]:
                return False
            fir_p = fir_p + 1
            sec_p = sec_p - 1
        return True

    # Check the first half, and compare with the second half
    # For example, 1212, the first half 12 = second half 12
    # 1234, first half 12 not = to second half 34
    # 
    def isPalindrome(self, x: int):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev_sec_half = 0
        while(x>rev_sec_half):
            rev_sec_half = rev_sec_half * 10 + x%10
            x = x // 10
        return x==rev_sec_half or x==rev_sec_half//10



if __name__ == "__main__":
    sol = Solution()
    x = -121
    x = 121
    x = 10
    print(sol.isPalindrome(x))
