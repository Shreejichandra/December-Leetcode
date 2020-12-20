'''
An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.
Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.
'''

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        corresponding_length = [1]
        for i in S[1:]:
            if corresponding_length[-1] >= K:
                break
            if i.isdigit():
                corresponding_length.append(corresponding_length[-1] * int(i))
            else:
                corresponding_length.append(corresponding_length[-1] + 1)
        
        print(corresponding_length)
        end = len(corresponding_length) - 1
        while corresponding_length[end] > K:
            end -= 1
            if corresponding_length[end] < K:
                #K = ((K-1) % corresponding_length[end]) + 1 
                K = K % corresponding_length[end]
                if K == 0:
                    K = corresponding_length[end]
        while S[end].isdigit():
            end -= 1
        return S[end]        
        
