##Ideas:
# Mentain two points, one pointing to the smaller number and the other one pointing to the larger number  (0, target)
# When the sum of square of two pointers are equal to the total cost, then return True
# If the sum of two points are smaller, move the left (smaller) pointer one step right
# If the sum of two points are larger, move the right (larger) pointer one step left
# The Key in this problem is the initial value for right pointer. We can set the right pointer to be sqrt(target) to reduce to time complicaty

from math import sqrt
class Solution:
    def judgeSquareSum(self, target: int):
        left_index = 0
        right_index = sqrt(target)
        int_right = int(right_index)
        if right_index == int_right:
            right_index = int_right
        else:
            right_index = int_right + 1

        # Can be equal
        while(left_index <= right_index):
            current_sum = left_index * left_index + right_index * right_index
            if current_sum == target:
                return True
            if current_sum > target:
                right_index = right_index - 1
            else:
                left_index = left_index + 1
        return False



if __name__ == '__main__':
    target = 2
    sol = Solution()
    print(sol.judgeSquareSum(target))
