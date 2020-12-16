'''
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
'''

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        song_time = defaultdict(int)
        ans = 0
        for i in time:
            reduced_time = i % 60
            if reduced_time == 0:
                find_time = 0
            else:
                find_time = 60-reduced_time
            
            if find_time in song_time:
                ans += song_time[find_time]
            song_time[reduced_time] += 1
            
        return ans
