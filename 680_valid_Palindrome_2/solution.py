##Ideas:
# Mentain two points, one from the beginning and one from the end
# If one pointer latter is equal to the other pointer letter, move left to one step right, move right to one step left
# continue
# If both pointer letters are not the same, at the first time, recusivly call is_palindrome(left) and is_palindrom(right)
# If both pointer letters are not the same again, return False


class Solution_V1:
    def __init__(self):
        self.first_diff = True
    def validPalindrome(self, s: str) -> bool:
        left_p = 0
        right_p = len(s) - 1
        while(left_p < right_p):
            if s[left_p] == s[right_p]:
                left_p = left_p + 1
                right_p = right_p - 1
            elif self.first_diff is True:
                self.first_diff = False
                ret_left = self.validPalindrome(s[left_p+1:right_p+1])
                if ret_left is True:
                    return True
                else:
                    return self.validPalindrome(s[left_p:right_p])
            else:
                return False
        return True


class Solution:
    # start and end must within range, it means the max value is end is len(s)-1
    def is_palindrome(self, s, start, end):
        while(start < end):
            if s[start] != s[end]:
                return False
            start = start + 1
            end = end - 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left_p = 0
        right_p = len(s) - 1
        while(left_p < right_p):
            if s[left_p] != s[right_p]:
                return self.is_palindrome(s, left_p, right_p-1) or self.is_palindrome(s, left_p+1, right_p)
            left_p = left_p + 1
            right_p = right_p - 1
        return True



if __name__ == '__main__':
    s = "hello"
    s = "abca"
    sol = Solution()
    print(sol.validPalindrome(s))



