##
# Idea: step 1. Create a hashmap, and store the number of each unique items
# loop the list, for each item, add the count by 1
# step 2: create a priority queue, put all the items in the previous map into priority queue
# step 3: return the top K items from the priority queue

## In python, Counter can do step 1 and heapq.nlargest can do step 2 and step 3 together

import heapq
from collections import Counter
class Solution:
    #def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def topKFrequent(self, nums, k: int):
        # O(1) time
        if k == len(nums):
            return nums

        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)

        if k == len(count):
            return list(count.keys())
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 3
    sol = Solution()
    print(sol.topKFrequent(nums, k))