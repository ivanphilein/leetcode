class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return None
        current_list = []
        current_list.append(root)
        ret_list = []
        line_list = []
        line_list.append(root.val)
        ret_list.append(line_list)
        current_list = root.children
        while(len(current_list)>0):
            line_list = []
            next_list = []
            for item in current_list:
                line_list.append(item.val)
                next_list.extend(item.children)
            ret_list.append(line_list)
            current_list = next_list
        return ret_list