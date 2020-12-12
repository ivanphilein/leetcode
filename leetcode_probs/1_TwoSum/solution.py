##Ideas:
# Brute Force method 1:
# Loop i from the first to the last, and inner second loop from (i+1) to the last, check whether the sum can be equal to the target
# Hash Table (Dict) method 2:
# Loop i from the first to the last
# Check if target-nums[i] exist in the dict or not
# If not, insert the nums[i]:i into the dict




class Solution:
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target: int):
        len_nums = len(nums)
        hash_dict = dict()
        for i in range(len_nums):
            first = nums[i]
            second = target - first
            if second in hash_dict.keys():
                return [hash_dict[second], i]
            hash_dict[first] = i
        return []



if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    nums = [2,7,11,15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))
