#####
# Ideas:
# Brute Force: 
# Loop i from the first to the last, and inner second loop from (i+1) to the last, and save the largest
# Tims O(n^2) and Space O(1)
#
# Idea 2:
# Sort first, and then use two pointers to find the result



class Solution:
    #def twoSumLessThanK(self, nums: List[int], k: int) -> int:
    # V1: Brute Force, Two loops, with O(n^2), space: O(1)
    def twoSumLessThanK_v1(self, nums, k):
        len_nums = len(nums)
        single_max = -1
        sum_max = -1
        for i in range(len_nums):
            first = nums[i]
            for j in range(i+1, len_nums):
                second = nums[j]
                this_sum = first + second
                if this_sum < k and this_sum > sum_max:
                    sum_max = this_sum
        return sum_max

    # V2: Sort, then use two pointers to find, with O(nlogn), space is O(logn) to O(n) depends on the sorting algorithm
    def twoSumLessThanK_v2(self, nums, k):
        nums.sort()
        len_nums = len(nums)
        fir_p = 0
        sec_p = len_nums - 1
        saved_sum = -1
        while(fir_p < sec_p):
            fir_v = nums[fir_p]
            sec_v = nums[sec_p]
            cur_sum = fir_v + sec_v
            if cur_sum >= k:
                sec_p = sec_p - 1
            else:
                if cur_sum > saved_sum:
                    saved_sum = cur_sum
                fir_p = fir_p + 1
        return saved_sum

    # V3: Counting Sort
    def twoSumLessThanK(self, nums, k):






if __name__ == '__main__':
    nums = [34,23,1,24,75,33,54,8]
    k = 60
    sol = Solution()
    print(sol.twoSumLessThanK(nums, k))



