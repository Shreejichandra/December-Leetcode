'''
QUESTION
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        def bfs(node):
            queue = deque()
            queue.append(node)
            output = []
            
            while queue:
                size = len(queue)
                curr = []
                for i in range(size):
                    popped = queue.popleft()
                    curr.append(popped)
                    if popped.left:
                        queue.append(popped.left)
                    if popped.right:
                        queue.append(popped.right)
                output.append(curr)
            return output
        output = bfs(root)
        # Shift the pointers
        for level in output:
            for i in range(len(level)-1):
                level[i].next = level[i+1]
            level[-1].next = None

        
        return output[0][0]       
