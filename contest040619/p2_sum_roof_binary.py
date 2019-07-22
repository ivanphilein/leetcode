import math
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution(object):
#     def sumRootToLeaf(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root is None:
#             return 0


#         node_list = []
#         node_list.append(None)
#         node_list.append(root)
#         next_index = 1
#         while(next_index < len(node_list)):
#             cur = node_list[next_index]
#             next_index = next_index + 1
#             if cur is None:
#                 continue
#             if cur.left is not None:
#                 node_list.append(cur.left)
#                 if cur.right is None:
#                     node_list.append(None)
#                 else:
#                     node_list.append(cur.right)
#             else:
#                 node_list.append(None)
#                 if cur.right is not None:
#                     node_list.append(cur.right)
#                 else:
#                     node_list.append(None)
            
#         leaf_list = []
#         for index in range(len(node_list)):
#             n = node_list[index]
#             if n is None:
#                 continue
#             if n.left is None and n.right is None:
#                 leaf_list.append(index)
#         node_len = len(node_list)
#         depth = int(math.log(node_len, 2) + 0.5) - 1
#         leaf_start = int(math.pow(2, depth))
#         leaf_end = node_len
#         result = 0
#         print "==="
#         print depth
#         print leaf_start
#         print leaf_end
#         for n in range(leaf_start, leaf_end):
#             #print "---"
#             #print n
#             if node_list[n] is None:
#                 continue
#             node_val = 0
#             p = 0
#             index = n
#             while(index > 0):
#                 val = node_list[index].val
#                 if val == 1:
#                     node_val = node_val + math.pow(2, p)
#                 p = p + 1
#                 index = index/2
#             result = result + node_val
#        return int(result)

        
class Solution(object):
    ans = 0
    mod = 1000000007
    def dfs(self, node, acc):
        if node is not None:
            acc = acc * 2 + node.val
            if node.left is None and node.right is None:
                self.ans = self.ans + acc
            dfs(node.left, acc)
            dfs(node.right, acc)

    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dfs(root, 0)
        return self.ans
        
        

if __name__ == '__main__':
    ob = Solution()
    val_node = [1,0,1,0,1,0,1]
    val_node = [0,1,0,0, "null", 0,0, "null" , "null" , "null" ,1,"null","null","null",1]
    
    print ob.sumRootToLeaf(node_list[0])
