#Given an array of integers arr, return true if and only if it is a valid mountain array.

class Solution:
    def validMountainArray(self, A: List[int]) -> int:
        n = len(A)
        ans = 0 
        for i in range(1, n-1):
            if A[i-1] < A[i] > A[i+1]:
                left = right = i
                while left > 0 and A[left] > A[left-1]:
                    left -= 1
                while right + 1 < n and A[right] > A[right+1]:
                    right += 1
                ans = max(ans, (right-left+1))
        return ans == n
