##Ideas:
# Recusive call to reverse a singl linked list
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Reverse a whole single linked list
    #def reverse(self, head: ListNode) -> ListNode:
    def reverse(self, head: ListNode):
        if head is None:
            return None
        if head.next is None:
            return head
        last = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return last

    def reverse_firstK(self, head: ListNode, k: int):
        if head is None:
            return None
        if k <= 1:
            return head
        ret_head = self.reverse_firstK(head.next, k-1)
        temp = head.next
        head.next= head.next.next
        temp.next = head
        return ret_head

    # reverse a single linked list between m to n
    #def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    def reverseBetween(self, head: ListNode, m: int, n: int):
        if m == 1:
            return self.reverse_firstK(head, n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head


if __name__ == "__main__":
    head = ListNode(1, None)
    head.next = ListNode(2, None)
    head.next.next = ListNode(3, None)
    head.next.next.next = ListNode(4, None)
    head.next.next.next.next = ListNode(5, None)
    #ret_str = ""
    #while(head is not None):
    #    ret_str = ret_str + str(head.val) + " -> "
    #    head = head.next
    #print("before")
    #print(ret_str)
    sol = Solution()
    #head = sol.reverse_firstK(head, 2)
    head = sol.reverseBetween(head, 2, 4)
    ret_str = ""
    while(head is not None):
        ret_str = ret_str + str(head.val) + " -> "
        print(head.val)
        head = head.next
    print("after")
    print(ret_str)
