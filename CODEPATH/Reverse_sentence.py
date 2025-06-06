''''''''''
 Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of the words reversed.
The sentence will contain only alphabetic characters and spaces to separate the words.
If there is only one word in the sentence, the function should return the original string

lower(): Converts a string to lowercase.
upper(): Converts a string to uppercase
split(): Splits a string into a list of substrings based on a delimiter.
join(): Joins elements of an iterable (like a list) into a single string using a separator. 
isalnum(): Checks if all characters in the string are alphanumeric.
isalpha(): Checks if all characters in the string are alphabetic.
isdigit(): Checks if all characters in the string are digits.
isspace(): Checks if the string contains only whitespace characters.
isupper(): Checks if all characters in the string are uppercase.
islower(): Checks if all characters in the string are lowercase. 
'''


# U - input is a str output is a string reversed
# P - one word, return the word, 
# I 


def reverse_sentence(sentence):
    # words = sentence.split() # O(n) n len of str
    # reversed_words = words[::-1]
    # return ' '.join(reversed_words)



    #word = list(sentence)
    #print(word)
    word = sentence.split() # O(n) n len of str
    #print(word)
    l = 0
    r = len(word) - 1

    while l < r:
        temp = word[l]
        word[l] = word[r]
        word[r] = temp
        l += 1
        r -= 1
    return ' '.join(word)

sentence = "tubby little cubby all stuffed with fluff"
result = reverse_sentence(sentence) # Expected Output: "fluff with stuffed all cubby little tubby"
print(result)

sentence = "Pooh"
result = reverse_sentence(sentence) # Expected Output: "Pooh"
print(result)



"""""""""
In the extended universe of fictional bears, Goldilocks finds an enticing list of numbers in the Three Bears' house. She doesn't want to take a number that's too high or 
too low - she wants a number that's juuust right. Write a function goldilocks_approved() that takes in the list of distinct positive integers nums 
and returns any number from the list that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

Return the selected integer.
"""
#return any thats not the min or max
#if we have len 2 (len < 3) we return -1
# if its empty? return -1
# Using min() and max()
# Loop through the list
# Sorting using sorted()
def goldilocks_approved(nums):
    if len(nums) < 3:
        return -1
    
    # sorted(nums)
    # min_num = min(nums)
    # max_num = max
    # count = 0
    min_num = min(nums)
    max_num = max(nums)
    # print(min_num)
    # print(max_num)
    for i in range(len(nums)): #min()
        if nums[i] != min_num and nums[i] != max_num:
            # if count == 1:
            return nums[i] #[3, 2, 1, 4]
            # else:
            #     count += 1
            

nums = [3, 2, 1, 4] 
#       l  r
result = goldilocks_approved(nums) # Expected Output: 2
print(result)

nums = [1, 2]
result = goldilocks_approved(nums) # Expected Output: -1
print(result)

nums = [2, 1, 3]
result = goldilocks_approved(nums) # Expected Output: 2
print(result)