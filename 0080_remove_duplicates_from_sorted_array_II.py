'''
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        count_curr_element = 1
        curr_element = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == curr_element:
                if count_curr_element <= 1:
                    count_curr_element += 1
                    i += 1
                else:
                    nums.pop(i)
            else:
                curr_element = nums[i]
                count_curr_element = 1
                i += 1
        return len(nums)
            
        
