##Ideas:
# Sol1: Pop each (x%10) into a queue (list) and push out one by one
# Time: O(logn), Space O(1)
# Sol2: 


class Solution:
    #def reverse(self, x: int) -> int:
    def reverse(self, x: int):
        max_num = 2**31
        if x < 0:
            neg_bool = True
            x = 0-x
        else:
            neg_bool = False
        store_list = []
        while(x>0):
            store_list.append(x%10)
            x = x // 10
        ret_x = 0
        time = 1
        while(len(store_list)>0):
            ret_x = ret_x + time*store_list.pop()
            time = time * 10
        if neg_bool is True:
            if ret_x > max_num -1:
                return 0
            return 0-ret_x
        else:
            if ret_x > max_num:
                return 0
            return ret_x




if __name__ == "__main__":
    sol = Solution()
    x = 120
    x = 1534236469
    print(sol.reverse(x))
