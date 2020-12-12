##Ideas:
# Recusive call to reverse a singl linked list
# There are three steps
# Step 1: reverse the first k nodes
# Step 2: Recusivly call the rest of n-k list
# Step 3: Combine the outputs from the previous two steps together

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Reverse the list between fir_node, to sec_node. [fir_node, sec_node), sec_node not included
    def reverseBetweenTwo(self, fir_node, sec_node):
        pre = None
        cur = fir_node
        nxt = fir_node
        while(cur!=sec_node):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    #def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    def reverseKGroup(self, head: ListNode, k: int):
        if head is None:
            return None
        a = head
        b = head
        for i in range(k):
            if b is None:
                return head
            b = b.next

        fir_head = self.reverseBetweenTwo(a, b)
        a.next = self.reverseKGroup(b, k)
        return fir_head


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
    head = sol.reverseKGroup(head, 2)
    ret_str = ""
    while(head is not None):
        ret_str = ret_str + str(head.val) + " -> "
        print(head.val)
        head = head.next
    print("after")
    print(ret_str)
