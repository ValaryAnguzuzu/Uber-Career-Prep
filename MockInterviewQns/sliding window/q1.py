# Given an array of integers and an integer k, return the number of unique subarrays 
# of size k that contain duplicate elements.

#nums = [1, 2, 1, 2, 3], k = 3 output = 2
#nums = [1, 2, 3, 1, 2], k = 3 output = 0
#nums = [1, 1, 1, 1], k = 2 output = 1
#nums = [4, 4, 2, 4, 4], k = 3 output = 3

#use sliding window and hsahmap to keep trck of freqs in the cur window
#iterate thru input arr using a sliding window of fixed size k
#for each window if the count > 1, add subarr to set
#store the tuple in a set to ensure we get only unique subarrays

#init empty set
#init a dict
#iterate thru nums using a sliding window of size k
#for each window add new element, add if its exceeds k remove l
from collections import defaultdict

def count_unique_subarrays(nums, k):
    n = len(nums)
    if n < k:
        return 0 

    unique_subarr = set()
    freq = defaultdict(int)
    l = 0
    dups = 0

    for r in range(n):   #[4, 4, 2, 4, 4], k = 3 output = 3
        
        freq[nums[r]] += 1 #add cur elemnt to dict
        if freq[nums[r]] == 2:
            dups += 1

        
#shriking the window if it exceeds k
        if r - l + 1 > k:
            if freq[nums[l]] == 2: 
                dups -= 1
            freq[nums[l]] -= 1

            if freq[nums[l]] == 0:
                del freq[nums[l]] 

            l += 1
            
            # cur window is valid, add subarr to set

        if r - l + 1 == k and dups > 0:
            unique_subarr.add(tuple(nums[l:r+1]))

    return len(unique_subarr)

print(count_unique_subarrays([1, 2, 1, 2, 3], 3))  # Output: 2
print(count_unique_subarrays([1, 2, 3, 1, 2], 3))  # Output: 0
print(count_unique_subarrays([1, 1, 1, 1], 2))  # Output: 1
print(count_unique_subarrays([4, 4, 2, 4, 4], 3))  # Output: 3


        
