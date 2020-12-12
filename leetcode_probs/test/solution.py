##Ideas:
# BFS search, from each node i, search all connected nodes (up to 8), and update their costs to be min(current_cost, cost_i+1)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    def buildTree(self, preorder, inorder):
        if preorder is None or inorder is None:
            return None
        len_pre = len(preorder)
        len_in = len(inorder)
        if len_pre == 0 or len_in==0:
            return None
        return self.build_recusive(preorder, inorder, 0, len_pre, 0, len_in)

    def build_recusive(self, preorder, inorder, pre_start, pre_end, in_start, in_end):
        #print(pre_start, pre_end, in_start, in_end)
        #print("====")
        if (pre_start >= pre_end) or (in_start >= in_end):
            return None
        root_val = preorder[pre_start]
        left_count = 0
        for i in range(in_start, in_end):
            if inorder[i] == root_val:
                left_count = i
                break
        left_count = left_count - in_start
        left_pre_start = pre_start + 1
        left_pre_end = pre_start + left_count + 1
        left_in_start = in_start
        left_in_end = in_start + left_count
        right_pre_start = left_pre_end
        right_pre_end = pre_end
        right_in_start = left_in_end + 1
        right_in_end = in_end
        return TreeNode(root_val, self.build_recusive(preorder, inorder, left_pre_start, left_pre_end, left_in_start, left_in_end), self.build_recusive(preorder, inorder, right_pre_start, right_pre_end, right_in_start, right_in_end))
        

if __name__ == "__main__":
    sol = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    print(sol.buildTree(preorder, inorder))


