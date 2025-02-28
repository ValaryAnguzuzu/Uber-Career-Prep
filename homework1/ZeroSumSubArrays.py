"""Question 3: ZeroSumSubArrays
Given an array of integers, count the number of subarrays that sum to zero.

Examples:
Input Array: [4, 5, 2, -1, -3, -3, 4, 6, -7]
Output: 2
(Subarrays: [5, 2, -1, -3, -3], [-3, 4, 6, -7])

Input Array: [1, 8, 7, 3, 11, 9]
Output: 0

Input Array: [8, -5, 0, -2, 3, -4]
Output: 2
(Subarrays: [0], [8, -5, 0, -2, 3, -4])"""

#at first i was thinking maybe i could use a sliding window to keep track of the sum of the subarray,
# that anytime i get a sum that is zero i would increment a counter
# i tried to implement that but i kept getting stuck
#
#took me way more than 40 mins, about 1.5hrs to come up with any approach

#But, after much thought; 
# we want to keep track of the sum of the subarray
#we can use prefix sum to keep track of the sum of the subarray...
#whenver we see a repeat of the prefix sum, we have a subarray that sums to zero
#so we can use a dictionary to keep track of the sum and the number of times we have seen that sum
#if the sum appears again, we increment the count of the sum by 1


from collections import defaultdict

def zeroSumSubArrays(arr):
    """
    technique: hashing One-directional Running Computation/Total

    time complexity is O(n) because we are iterating through the array once
    space complexity is O(n) because we are storing the prefix sum in a list
    after knowing some hints, i took 30mins to fully implement this solution
    approach is to use prefix sum to keep track of the sum of the subarray 
    """ 
    #populate prefix subarray

    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]

    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]

    #initialize a dictionary to keep track of the sum and the number of times we have seen that sum
    sum_dict = defaultdict(int)
    zeroSum = 0

    for psum in prefix_sum:
        if psum == 0: #assuming arr = [0, 0, 0, 0, 0] we increment zeroSum by 1 everytime we get the 0
            zeroSum += 1

        zeroSum += sum_dict[psum]
        sum_dict[psum] += 1

    return zeroSum

#note: THIS WAS THE HARDEST PROBLEM FOR ME; I WAS NOT GETTING IT INTUITIVELY at first



print(zeroSumSubArrays([4, 5, 2, -1, -3, -3, 4, 6, -7]))  # Output: 2
print(zeroSumSubArrays([1, 8, 7, 3, 11, 9]))  # Output: 0
print(zeroSumSubArrays([8, -5, 0, -2, 3, -4]))  # Output: 2
print(zeroSumSubArrays([0, 0, 0, 0]))  # Output: 10 (Multiple overlapping subarrays)
print(zeroSumSubArrays([-1, 1, -1, 1])) # Output: 4