# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0]) 
  
        arr = [] 
  
        arr.append(root) 
  
        i = 1
        while ( i < len(preorder)):  
            temp = None
    
            while (len(arr) > 0 and preorder[i] > arr[-1].val):  
                temp = arr.pop() 
              
            if (temp != None):  
                temp.right = TreeNode(preorder[i]) 
                arr.append(temp.right) 
              
            else : 
                temp = arr[-1] 
                temp.left = TreeNode(preorder[i]) 
                arr.append(temp.left) 
            i = i + 1
          
        return root 
      
