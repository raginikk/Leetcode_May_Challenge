# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def InorderTraversal(node,arr):
    if node:
        InorderTraversal(node.left,arr)
        arr.append(node.val)
        InorderTraversal(node.right,arr)
    return arr    
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        arr=[]
        x = InorderTraversal(root,arr)
        
        return x[k-1]
        
      
