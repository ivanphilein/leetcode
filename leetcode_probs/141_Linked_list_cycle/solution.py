##Ideas:
# Solution 1,  two pointers, loop O(n^2), fix one pointer and loop the other one, check whether two pointers are same or not
# Solution 2: O(1), two pointers, one pointer goes one step each time, the other point goes two steps each time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        fir_p = head
        sec_p = head.next
        while(fir_p is not None and sec_p is not None):
            if fir_p.val == sec_p.val and fir_p.next == sec_p.next:
                return True
            if sec_p.next is None:
                return False
            fir_p = fir_p.next
            sec_p = sec_p.next.next
        return False



