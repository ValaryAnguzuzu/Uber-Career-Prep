# Given an integer array nums and an integer k, return true if there are two distinct 
# indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true  {1:0, 2:1 3:2}
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false    {1:0, 2:1, 3:2, 2:4}
 #3-0 = 3<=2? no
#we can use dict

def containsNearbyDuplicate(nums, k):
    """"
    TC = O(n)
    SC = O(n) - the dict
    """
    
    dict = {}
    for i, num in enumerate(nums):
        if num in dict and abs(i - dict[num]) <= k:
            return True
        dict[num] = i
    
    return False



#sliding window?
    seen = set(nums)

    

print(containsNearbyDuplicate([1,2,3,1], 3)) #true
print(containsNearbyDuplicate([1,0,1,1], 1)) #true
print(containsNearbyDuplicate([1,2,3,1,2,3], 2)) #false

