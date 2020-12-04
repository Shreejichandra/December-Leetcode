'''
Given two positive integers n and k.

A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.
'''

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        all_factors = []
        for i in range(1, (n//2)+1):
            if n % i == 0:
                all_factors.append(i)
        all_factors.append(n)
        if k > len(all_factors):
            return -1
        return all_factors[k-1]
