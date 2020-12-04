#Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        self.head = head
        self.all_nodes = []
        temp = head
        while temp != None:
            self.all_nodes.append(temp.val)
            temp = temp.next
        

    def getRandom(self) -> int:
        return random.choice(self.all_nodes)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
