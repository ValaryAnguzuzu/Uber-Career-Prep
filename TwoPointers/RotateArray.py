# Given an integer array nums, rotate the array to the right by k steps,
#  where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

#new arr
#move the elements to i + k pos of new arr until we reach end of arr
#then to know where to put the rest pf the elements, take i % len(nums); gives us the idx to place it
#then copy to original arr




#we can reverse 3 times
#so first reverse the k elements to come to the front of arr
#then reverse this k potion to be in expected order, amd the rest of arr to be in expected order too
   # [1,2,3,4,5,6,7], k = 3  #use k % len(nums) to know the exact posn of the k ekemts after first rotation
   # [7,6,5,4,3,2,1] -> [5,6,7,1,2,3,4]

def RotateArray(nums, k):
    """
    TC = O(N) #we traverse once
    SC = O(1)
    """
    n = len(nums)
    k = k % n

    l = 0
    r = n - 1


    #first rotation
    while l < r:
        nums[l], nums[r] = nums[r], nums[l] #-> [7,6,5,4,3,2,1]
        l += 1
        r -= 1

    #rotate the k portion
    l = 0
    r = k - 1 #if k = 3, r = idx 2

    while l < r:
        nums[l], nums[r] = nums[r], nums[l] #-> [5,6,7,4,3,2,1]
        l += 1
        r -= 1

    #reverse the last portion of arr

    l = k
    r = n - 1

    while l < r:
        nums[l], nums[r] = nums[r], nums[l] #-> [5,6,7,1,2,3,4]
        l += 1
        r -= 1

    return nums



print(RotateArray([1,2,3,4,5,6,7], 3)) #[5,6,7,1,2,3,4]
print(RotateArray([-1,-100,3,99], 2)) #[3,99,-1,-100]