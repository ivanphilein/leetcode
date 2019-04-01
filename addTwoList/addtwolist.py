# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
        ret_node = None
        cursor = ret_node
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        addition = 0
        
        p_sum = l1.val + l2.val + addition
        ret_node = ListNode(p_sum % 10)
        addition = p_sum/10
        cursor = ret_node
        l1 = l1.next
        l2 = l2.next
    
        while(l1 is not None and l2 is not None):
            p_sum = l1.val + l2.val + addition
            cursor.next = ListNode(p_sum % 10)
            addition = p_sum/10
            cursor = cursor.next
            l1 = l1.next
            l2 = l2.next
        if addition > 0:
            cursor.next = ListNode(addition)
        return ret_node

def printNode(node):
    cursor = node
    ret_str = ""
    while (cursor is not None):
        ret_str = str(cursor.val) + ret_str
        cursor = cursor.next
    return ret_str
if __name__ == "__main__":
    l1 = ListNode(8)
    l1.next = ListNode(4)
    l1.next.next = ListNode(8)
    print printNode(l1)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print printNode(l2)
    sum_node = addTwoNumbers(l1, l2)
    print printNode(sum_node)