##Ideas:
# Binary Search Tree, all nodes in the sub-left tree are smaller than the root and all nodes in the sub-right tree are larger than or equal to the root
# Solution: Divid and conquer
# Pick a value as root, then group all smller values as left tree and all larger or equal values are right tree, then build left and right tree



#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #def generateTrees(self, n: int) -> List[TreeNode]:
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.gene_sub_trees(1, n)

    def gene_sub_trees(self, start, end):
        if start > end:
            return [None]
        ret_trees = []
        for r in range(start, end+1):
            left_trees = self.gene_sub_trees(start, r-1)
            right_trees = self.gene_sub_trees(r+1, end)
            for left_t in left_trees:
                for right_t in right_trees:
                    ret_trees.append(TreeNode(r, left_t, right_t))
        return ret_trees



if __name__ == "__main__":
    sol = Solution()
    input_val = 3
    trees = sol.generateTrees(input_val)
