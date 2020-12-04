'''
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        all_nodes = []
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            all_nodes.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        new_head = TreeNode(all_nodes.pop(0))
        temp = new_head
        for i in all_nodes:
            temp.right = TreeNode(i)
            temp = temp.right
        return new_head
            
            
            
        
