# Idea:
# Step 1: loop from the end to the beginning, find the first element (with index i) which is smaller than the next element
# Step 2: loop from the next element to the end, find the the first element (with index j) which is smaller than the ith element. 
# Step 3: replace the ith and the (j-1)th elements
# Step 4: reverse the subsequence from i+1 to the end, because the original subsequence is in descrease order, now we reverse it to be increase order

class Solution:
    def switch(self, nums, i, j):
        nums[i] = nums[i] + nums[j]
        nums[j] = nums[i] - nums[j]
        nums[i] = nums[i] - nums[j]

    #def nextPermutation(self, nums: List[int]) -> None:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return None
        nums_len = len(nums)
        if nums_len == 1:
            return nums
        keep_i = -1
        for i in range(nums_len-2, -1, -1):
            if nums[i] < nums[i+1]:
                keep_i = i
                break
        if keep_i < 0:
            last_in = nums_len - 1
            for j in range(nums_len):
                if j >= last_in:
                    break
                self.switch(nums, j, last_in)
                last_in = last_in - 1
        else:
            re_in = -1
            for j in range(keep_i + 1, nums_len):
                if nums[j] <= nums[keep_i]:
                    re_in = j - 1
                    break
            if re_in == -1:
                re_in = nums_len - 1
            self.switch(nums, keep_i, re_in)
            last_in = nums_len - 1
            for j in range(keep_i+1, nums_len):
                if j >= last_in:
                    break
                self.switch(nums, j, last_in)
                last_in = last_in - 1


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 4, 2, 3, 2]
    nums = [1, 2, 5, 7, 6, 2]
    nums = [1, 2, 6, 4, 4, 5]
    #nums = [3, 2, 1]
    #nums = [1, 3, 2]
    for i in range(10):
        sol.nextPermutation(nums)
        print(nums)