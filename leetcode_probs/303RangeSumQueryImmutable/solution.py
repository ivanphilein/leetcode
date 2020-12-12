##Ideas:
# Sum range between i to j, it equals to sum range from 0 to j - sum range from 0 to i


class NumArray:
    #def __init__(self, nums: List[int]):
    def __init__(self, nums):
        self.nums = nums
        nums_len = len(nums)
        self.sum_list = None
        if nums_len > 0:
            sum_list = [0] * len(nums)
            sum_list[0] = nums[0]
            for i in range(1, nums_len):
                sum_list[i] = sum_list[i-1] + nums[i]
            self.sum_list = sum_list

    #def sumRange(self, i: int, j: int) -> int:
    def sumRange(self, i: int, j: int):
        sum_list = self.sum_list
        if i > 0:
            min_v = sum_list[i-1]
        else:
            min_v = 0
        return sum_list[j] - min_v


if __name__ == "__main__":
    all_nums = [-2, 0, 3, -5, 2, -1]
    start = 0
    end = 2
    start = 2
    end = 5
    sol = NumArray(all_nums)
    print(sol.sumRange(start, end))
