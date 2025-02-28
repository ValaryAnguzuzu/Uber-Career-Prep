"""Question 1: MaxMeanSubArray
Given an array of integers and an integer, k, find the maximum mean of a subarray of size k.

Examples:
Input Array: [4, 5, -3, 2, 6, 1]
Input k = 2
Output: 4.5

Input Array: [4, 5, -3, 2, 6, 1]
Input k = 3
Output: 3

Input Array: [1, 1, 1, 1, -1, -1, 2, -1, -1]
Input k = 3
Output: 1

Input Array: [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
Input k = 5
Output: 1"""


#here the size k will not be changing; its likely a sliding window Fixed size k;
#using two ptrs, it means the distance between them will always be k
#leading ptr r will start at k - 1 and trailing l at 0
#to keep track of max mean...we can have a variable maxMean init to 0 at the start
#at each iteration, before we move our ptrs, we want to compute mean; sum/k and have our curMean
#update its value by taking max between itself and the CurMean

#return maxmean

#how do i get sum?
#how about we keep track of the sums up until where we are; ie prefix Sum - no....maybe
   #better approach:
        #we can get the sum of the first window and store it in a variable
        #then we can slide the window
                 #For each subsequent position, subtract the element going out of the
      #  window and add the new element entering the window.
#then we can know the exact sum of the window and just do sum/ k
#


def maxMeanSubArr(nums, k):
    n = len(nums)
    """
    Technique: Fixed-size Sliding Window using Two Pointers (l and r)
    Time Complexity: O(n) - single pass thru array
    Space Complexity: O(1)
    time - 45mins
    """
    
    #can the input ever not have enough elements to make the required subarr? assuming so...
    if n < k:
        return None

    #compute the sum of our first window
    window_sum =  sum(nums[:k])
    max_mean = window_sum / k

    l = 0
    for r in range(k, n):
        #slide over the window
        window_sum += nums[r] - nums[l] #get the sum of cur window
        curr_mean = window_sum / k 

        max_mean = max(max_mean, curr_mean)

        l += 1

    return max_mean



print(maxMeanSubArr([4, 5, -3, 2, 6, 1], 2))  # Output: 4.5
print(maxMeanSubArr([4, 5, -3, 2, 6, 1], 3))  # Output: 3
print(maxMeanSubArr([1, 1, 1, 1, -1, -1, 2, -1, -1], 3))  # Output: 1
print(maxMeanSubArr([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5))  # Output: 1
print(maxMeanSubArr([], 3))  # Output: None
print(maxMeanSubArr([1], 1))  # Output: 1







