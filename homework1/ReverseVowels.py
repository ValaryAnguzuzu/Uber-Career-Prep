"""Question 2: ReverseVowels
Given a string, reverse the order of the vowels in the string.

Examples:
Input String: "Uber Career Prep"
Modified String: "eber Ceraer PrUp"

Input String: "xyz"
Modified String: "xyz"

Input String: "flamingo"
Modified String: "flominga""""

#our window will keep varying in size;
    #variable-size sliding window because the window
    #  shrinks and grows based on whether the characters are vowels(condition)
#two pointers one from the end of the input the other from the beginning of the input
      #forward-backward two pinter
#at each stage we compare the two and check first if its a vowel; if yes, swap the two if not move whatever pointer that is not currently 
#on a vowel

   #if both s[r] and s[l] are vowels, swap them
   #if only one is a ptr, move the other one
   #shld we worry about spaces?

#a set shld help us do faster lookup of the vowel


#strs are immutable; so we cnvert s to a list
def reverseVowels(s):
    """
    Technique: Two Pointers (l and r) - Forward/backward two-pointer
    Time Complexity: O(n) - single pass thru string
    Space Complexity: O(n) - list conversion
    time - 40mins
    """

    s = list(s)
    vowels = set("aeiouAEIOU")

    n = len(s) 
    l = 0
    r = n - 1
    while l < r:
        if s[l] not in vowels:
            l += 1
        elif s[r] not in vowels:
            r -= 1
        else:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    return "".join(s)

print(reverseVowels("Uber Career Prep"))  # Output: "eber Ceraer PrUp"
print(reverseVowels("xyz"))              # Output: "xyz"
print(reverseVowels("flamingo"))         # Output: "flominga"
print(reverseVowels("aeiou"))            # Output: "uoiea"



    



        

        



