# You are given a string s and an integer k. You can choose any character of the string and change it to any 
# other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.


# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

"""
:                 AABA BBA
 1. how do you if the substring is valid? len(othercharacters) <= k

 2. how do move the slinding window to get the max?

 #valid:       A A B A B B A 
               r
               l

        #hashmp--> to keep track of chars count

        #start them off at 0 with r for loop
        #check if substring is valid:
            #if yes,update freq get length and update maxlen
            #if not, 
            #       while loop (while invalid) decrement freq, move left till its valid

        return maxlen 
isvalid?(s,k)
AABA k-1: 
binheap? 
(a,1, a,2,.. a,3,b,1)

    A A B A B B A 
               r
               l

"""

def characterReplacement(s, k):
    
    count = {} #keep track of most freq char in substr
    maxlen = 0 #keep track of max len
    l = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1

        window_size = r - l + 1

        max_freq = max(count.values())

        # is the window is valid for replacement?
        while window_size - max_freq > k:
            count[s[l]] -= 1
            l += 1
            
        maxlen = max(maxlen, window_size)

    return maxlen

"""
BRUTE FORCE
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count, maxf = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                maxf = max(maxf, count[s[j]])
                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)
        return res

"""

       
       
       
       
       





