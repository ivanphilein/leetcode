##Ideas:
# Because the list 1 contains enough space, and all valid elements in list 1 are at the beginning of list 1, therefore, we can directly copy element to the end of list 1 if we loop both lists from end to beginning
# mentain two pointers from the end of both lists, which one is bigger, put it to the last valid location (m+n-1)

class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        fir_p = m - 1
        sec_p = n - 1
        to_loc = m + n - 1
        while(fir_p >=0 and sec_p>=0):
            fir_item = nums1[fir_p]
            sec_item = nums2[sec_p]
            if fir_item <= sec_item:
                nums1[to_loc] = sec_item
                sec_p = sec_p - 1
            else:
                nums1[to_loc] = fir_item
                fir_p = fir_p - 1
            to_loc = to_loc - 1

        ## Not necessary
        #while(fir_p >= 0):
        #    nums1[to_loc] = nums1[fir_p]
        #    to_loc = to_loc - 1
        #    fir_p = fir_p - 1

        while(sec_p >= 0):
            nums1[to_loc] = nums2[sec_p]
            to_loc = to_loc - 1
            sec_p = sec_p - 1




if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    sol = Solution()
    print(sol.merge(nums1, m, nums2, n))
    print(nums1)



