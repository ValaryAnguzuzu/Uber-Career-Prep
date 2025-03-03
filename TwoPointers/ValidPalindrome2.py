# Given a string s, return true if the s can be palindrome after deleting
#  at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false

#normal way to check palindroe but whever we encounter a misatch, we want tp check that substring
#if we rempve l or r is the remainder still valid palindrome?
  #2 pointer technique

def is_Palindrome(s):
    """
    TC: O(N) 
    SC: O(1)
    """

    #helper func for normal palindrome check
    def validPalindrome(l, r):
        while l < r:
            if s[l] != s[r]:  #O(n)
                return False
            l += 1
            r -= 1
        return True

    #now we check our str using 2 ptrs

    l = 0
    r = len(s) - 1

    while l < r:   #O(n)
        if s[l] != s[r]:
            #check valid palindrome on this substring if we removed either the left or right chsr
            #basically; Try skipping either character and check if the rest forms a palindrome

            return validPalindrome(l+1,r) or validPalindrome(l, r-1)

        l += 1
        r -= 1

    return True #no mismatches, s is already a valid palindrome

print(is_Palindrome("aba")) #True
print(is_Palindrome("abca")) #True
print(is_Palindrome("abc")) #False


    