class Solution:
    #def findMin(self, nums: List[int]) -> int:
    def find_min_patition(self, nums, start, end):
        n = end - start + 1
        if n == 1:
            return nums[start]
        if n == 2:
            return min(nums[start], nums[end])
        half_n = int(n/2) + start
        if nums[start] <= nums[half_n] and nums[half_n+1] <= nums[end]:
            return min(nums[start], nums[half_n+1])
        elif nums[start] <= nums[half_n]:
            if half_n+1 >= end:
                return nums[end]
            else:
                return self.find_min_patition(nums, half_n+1, end)
        else:
            if start >= half_n:
                return nums[start]
            else:
                return self.find_min_patition(nums, start, half_n)

    def findMin(self, nums):
        return self.find_min_patition(nums, 0, len(nums)-1)


if __name__ == "__main__":
    nums = [6, 7, 0, 1, 2, 3]
    nums = [1,2]
    nums = [2,3,4,5,1]
    sol = Solution()
    print(sol.findMin(nums))