"""Question 7: KAnagrams
Two strings are considered to be “k-anagrams” if they can be made into anagrams by changing at most k characters in one of the strings. 
Given two strings and an integer k, determine if they are k-anagrams.

Examples:
Input Strings: "apple", "peach"
Input k: 1
Output: False

Input Strings: "apple", "peach"
Input k: 2
Output: True

Input Strings: "cat", "dog"
Input k: 3
Output: True

Input Strings: "debit curd", "bad credit"
Input k: 1
Output: True

Input Strings: "baseball", "basketball"
Input k: 2
Output: False"""

#keep track of the freqs of each letter - anagrams shld have same letter freq
#so two dicts with freqs
#iterate thru btoh and see if the same letter appears in both, if so
#reduce the freq of the letter in dict1 by that of dict2; this way we cn track how many letters can be switched
#at the end, if the number of switchable letters is  equal to k, return True

def k_anagrams(s, t, k):
    """
    technique used: Hashing Technique (Two arrays/strings increment/decrement hashmap counts)
    time complexity is O(n) because we are iterating through the strings once
    space complexity is O(n) because we are storing the freq of the letters in a dictionary
    time taken: 40mins
    """
    #base case if the two lens are different in anagram check, we just return false
    if len(s) != len(t):
        return False

    #initialize two dictionaries to keep track of the freq of each letter in the strings
    dictS = {}
    dictT = {}

    for letter in s:
        if letter in dictS:
            dictS[letter] += 1
        else:
            dictS[letter] = 1

    for letter in t:
        if letter in dictT:
            dictT[letter] += 1
        else:
            dictT[letter] = 1

    #iterate thru the two dicts and see if the same letter appears in both, if so
    for letter in dictS:
        if letter in dictT:
            #reduce the freq of the letter in dict1 by that of dict2
            dictS[letter] -= dictT[letter]

    #at the end, if the number of switchable letters is  equal to k, return True
    count = 0
    for key in dictS:
        if dictS[key] > 0:
            count += dictS[key] # counting the remaining switchable characters

    return count == k 


# Provided Test Cases :
print(k_anagrams("apple", "peach",1)) # expected: False
print(k_anagrams("apple", "peach",2)) # expected: True
print(k_anagrams("cat", "dog", 3)) # expected: True
print(k_anagrams("debit curd", "bad credit",1)) # expected: True
print(k_anagrams("baseball", "basketball", 2)) # expected: False
