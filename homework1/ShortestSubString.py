# ShortestSubstring
# Given a string and a second string representing required characters, 
# return the length of the shortest 
# substring containing all the required characters.

# Examples:
# Input Strings: "abracadabra", "abc" 
# Output: 4
# (Shortest Substring: "brac")

# Input Strings: "zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx" (Fun fact: "Zzyzx" is a town in the Mojave Desert in California!)
# Output: 10
# (Shortest Substring: "zzxwdcbxyz")

# Input Strings: "dog", "god"
# Output: 3
# (Shortest Substring: "dog")

#keep track of min length
#keep track of how any times the required chars occur
#track how many required chars are in the cur window
#once all the required chars are present eg abrac try removing from the left inthis case a
def ShortestSubstring(s, req):
    """
    technique: two pointers
    time complexity = O(n + m) where: n = length of s m = length of req
    space complexity = O(n) - space for the dict storing the required chars
    time = 1hr10ins
    """

    #freq map for required chars
    freq = {}
    for char in req:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    needed = len(req) #we need to have the total num of required chars in the window 
    l = 0
    min_len = float('inf') #init to a very large num

    for r in range(len(s)): #increase our window size
        if s[r] in freq: #if the char is in the required chars
            freq[s[r]] -= 1 #reduce the freq of the char in the freq map
            if freq[s[r]] >= 0: #if the freq of the char is greater than or equal to 0
                needed -= 1 #reduce the number of required chars in the window

        #if we have all required chars, we ca try shrinking the window
        while needed == 0:
            min_len = min(min_len, r - l + 1)

            #if the left char is in the freq map
            if s[l] in freq:
                freq[s[l]] += 1 #restore freq since its leaving thw window

                if freq[s[l]] > 0: #if count is > 0 means a needed character was removed, increase needed
                    needed += 1

            l += 1 #move the left pointer to the right

    return min_len

print(ShortestSubstring("abracadabra", "abc")) #4
print(ShortestSubstring("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx")) #10
print(ShortestSubstring("dog", "god")) #3
