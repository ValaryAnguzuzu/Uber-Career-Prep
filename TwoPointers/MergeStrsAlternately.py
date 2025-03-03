# You are given two strings word1 and word2. Merge the strings 
# by adding letters in alternating order, starting with word1. If a string is
#  longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 
#iterate thru both strs simultaenously
# str to store our output str
#append the current char from word1 and word2 to the result string


def mergeAlternately(word1, word2):
    """
    TC: O(N+M) - we are iterating thru both strs once
    SC = O(N+M) - we are storing the merged string in a new str
    """
    i = 0
    merged = ""

    while i < len(word1) and i < len(word2):
        merged += word1[i]
        merged += word2[i]

        i += 1

    if i < len(word1):
        merged += word1[i:]

    if i < len(word2):
        merged += word2[i:]


    return merged

print(mergeAlternately("abc", "pqr")) #apbqcr
print(mergeAlternately("ab", "pqrs")) #apbqrs
print(mergeAlternately("abcd", "pq")) #apbqcd
print(mergeAlternately("ab", "p")) #apb
print(mergeAlternately("a", "p")) #ap
print(mergeAlternately("a", "pq")) #apq
