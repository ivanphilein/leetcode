##Ideas:
# For each item, there are two options, either rob or not rob. Just pick the highest between those two options



class Solution:
    #def rob(self, nums: List[int]) -> int:
    def rob(self, nums):
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        rob_pre1 = 0
        rob_pre2 = 0
        for i in range(nums_len):
            rob_t = rob_pre2 + nums[i]
            rob_f = rob_pre1
            rob_this = max(rob_t, rob_f)
            rob_pre2 = rob_pre1
            rob_pre1 = rob_this
        return rob_this


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    nums = [2,7]
    nums = [2,1,1,2]
    nums = [1,1,1,2]
    sol = Solution()
    print(sol.rob(nums))
