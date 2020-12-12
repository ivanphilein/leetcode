##Ideas:
# Solution: Divid and conquer
# The differences between Divid and Conquer (DC) with Dynamic Programming (DP) are whether the subproblems share the same sub-subproblems or not. 
# The key of DP is, different sub-problems share the same sub-sub-problems. Then, we need to run it from bottom to up, and save all the solved sub-problems somewhere, then the new probelms can direct use those solutions without re-calculation
# The key of DC is, different sub-problems do not share the same sub-sub-problems. Then, we can calculate is from top to bottom. In this problems, does it have shared sub-problems? No, it doesn't, because the left and right sub-sequences are total independence with each other

class Solution:
    #def diffWaysToCompute(self, input: str) -> List[int]:
    def diffWaysToCompute(self, input):
        ways = []
        str_len = len(input)
        for i in range(str_len):
            c = input[i]
            if c == '+' or c == '-' or c == "*":
                left_ways = self.diffWaysToCompute(input[0:i])
                right_ways = self.diffWaysToCompute(input[i+1:])
                for l in left_ways:
                    for r in right_ways:
                        if c == "+":
                            ways.append(l+r)
                        elif c == "-":
                            ways.append(l-r)
                        elif c == "*":
                            ways.append(l*r)
        if len(ways) == 0:
            ways.append(int(input))
        return ways


if __name__ == "__main__":
    sol = Solution()
    input_str = "2-1-1"
    input_str = "2*3-4*5"
    print(sol.diffWaysToCompute(input_str))
