

# Prompt:

# Given an array of integers nums and an integer k, return the length of the longest contiguous subarray such that the sum of its elements is less than or equal to k.

# Input: nums = [1, 2, 1, 0, 1, 1, 0], k = 4  
#                l
# Output: 5  
# Explanation: The subarray [2, 1, 0, 1, 0] has a sum of 4 and length 5.

# Input: nums = [2, 3, 1, 2, 4, 3], k = 7  
# Output: 3  
# Explanation: The subarray [1, 2, 4] has a sum of 7 and length 3, but [3,1,2] has sum 6 and length 3.


 #nums = [1, 2, 1, 0, 1, 1, 0], k = 4 
         # l
def longest_subarr(nums, k):  
    l = 0
    maxsum = 0

    maxlen = 0

    for r in range(len(nums)):
        maxsum += nums[r]
        if maxsum <= k:
            maxlen = max(maxlen, r - l + 1)

        else:
            maxsum -= nums[l]
            l += 1
            #maxlen = max(maxlen, r - l + 1) #we're only interested inmaxlen if its valid

    return maxlen

print(longest_subarr([1, 2, 1, 0, 1, 1, 0], 4)) #5
print(longest_subarr([2, 3, 1, 2, 4, 3], 7)) #3
print(longest_subarr([1, 1, 1, 1, 1, 1, 1, 1, 1], 1)) #1
print(longest_subarr([50, 50, 50, 50], 1)) #0
print(longest_subarr([50, 50, 50, 50], 1000)) #4


#edge cases --> come up with edge cases(think abt those extreme scenarios)!!




        




