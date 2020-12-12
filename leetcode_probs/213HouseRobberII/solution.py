##Ideas:
# For each item, there are two options, either rob or not rob. Just pick the highest between those two options
# All houses arrange as a cycle. Then remove the first house or not, run no-cycle test from 0 to n-1, then test from 1 to n. Pick the bigger one
# Consider non-cycle: rob_n = max(nc1(n-1), nc2(n))



class Solution:
    #def rob(self, nums: List[int]) -> int:
    def rob_nc(self, nums, start=0):
        nums_len = len(nums) - 1 + start
        rob_pre1 = 0
        rob_pre2 = 0
        nc_list = []
        for i in range(start, nums_len):
            rob_t = rob_pre2 + nums[i]
            rob_f = rob_pre1
            rob_this = max(rob_t, rob_f)
            rob_pre2 = rob_pre1
            rob_pre1 = rob_this
            nc_list.append(rob_this)
        return nc_list
    def rob(self, nums):
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        if nums_len == 1:
            return nums[0]
        nc_s0 = self.rob_nc(nums, 0)
        nc_s1 = self.rob_nc(nums, 1)
        return max(nc_s0[-1], nc_s1[-1])


if __name__ == "__main__":
    nums = [2, 3, 2]
    nums = [1,2,3,1]
    nums = [0]
    sol = Solution()
    print(sol.rob(nums))
