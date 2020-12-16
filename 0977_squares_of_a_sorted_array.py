#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            square_of_num = i * i
            ans.append(square_of_num)
        return sorted(ans)
        
