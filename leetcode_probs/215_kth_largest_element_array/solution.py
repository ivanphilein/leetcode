##Ideas:
# The returned j here means num_list[j] <= num_list[j+i] and num_list[j] > num_list[j-i] for all i > 0
# j can be used to find the jth smallest number. Find the smallest instead of the largest because it is easier.
# the jth is directly the jth smallest, if finding the the number of largest, needs to use len(num_list)- l - 1
# In this function, all numbers equal to the num_list[0] are placed at the left side
def patition(num_list, start, end):
    i = start
    j = end + 1
    while(True):
        i = i + 1
        j = j - 1
        while(num_list[i]<=num_list[start] and i<end):
            i = i + 1
        while(num_list[j]>num_list[start] and j>start):
            j = j - 1
        if i >= j:
            break
        swap(num_list, i, j)
    swap(num_list, start, j)
    return j

def swap(num_list, i, j):
    temp = num_list[i]
    num_list[i] = num_list[j]
    num_list[j] = temp

class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    def findKthLargest(self, nums, k):
        k = len(nums) - k
        start = 0
        end = len(nums) - 1
        while(start < end):
            j = patition(nums, start, end)
            if j == k:
                break
            elif j < k:
                start = j + 1
            else:
                end = j - 1
        return nums[k]



if __name__ == '__main__':
    nums = [5, 5, -1, 10, 2, 2, 2, 2, 2, 4]
    k = 4
    sol = Solution()
    print(sol.findKthLargest(nums, k))
