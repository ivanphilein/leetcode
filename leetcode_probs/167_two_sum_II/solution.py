#####
####Problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

##Ideas:
####Mentain two points, one pointing to the smaller number and the other one pointing to the larger number
####When the sum of two points are equal to the total cost, then return
####If the sum of two points are smaller, move the left (smaller) pointer one step right
####If the sum of two points are larger, move the right (larger) pointer one step left

class Solution:
    def twoSum(self, num_list, target):
        left_index = 0
        right_index = len(num_list) - 1
        current_sum = num_list[left_index] + num_list[right_index]
        while(current_sum != target):
            if current_sum > target:
                right_index = right_index - 1
            else:
                left_index = left_index + 1
            if left_index == right_index:
                return None
            current_sum = num_list[left_index] + num_list[right_index]
        return [left_index+1, right_index+1]



if __name__ == '__main__':
    num_list = [2, 3, 4]
    target = 6
    sol = Solution()
    print(sol.twoSum(num_list, target))



