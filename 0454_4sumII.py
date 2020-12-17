'''
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
'''

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        possible_sum = defaultdict(int)
        ans = 0
        for i in range(len(A)):
            for j in range(len(B)):
                total = A[i] + B[j]
                possible_sum[total] += 1
        
        for i in range(len(C)):
            for j in range(len(D)):
                find = -(C[i] + D[j])
                if find in possible_sum:
                    ans += possible_sum[find]
        return ans
                
                
        
