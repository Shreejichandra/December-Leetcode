'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.
'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        first = float("inf")
        second = float("inf")
        for i in nums:
            if i < first:
                first = i
            elif first < i < second:
                second = i
            elif first < second < i:
                return True
        return False
