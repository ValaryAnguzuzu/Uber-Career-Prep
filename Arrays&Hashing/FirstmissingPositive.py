# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 
# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.

"""
step1:
we want to rearrange our input, do it in place
place each number nums[i] at idx i-1 if its within the valid range of [1,n]; because the smallest postive num will always be 1 and the largest n+1
this ensure direct mapping between indices and the numbers makinf it easy to find the first positive

HOW:
iterate thru nums with a while loop, to keep in range
for each nums[i] check some coditions:
    that nums[i] is both >= 1 ad <= n and that nums[i] != nums[i-1]
    if condition is met, swap the two to take nums[i] to its correct psn
    otherwise move to the next element
    repeat unitl all numbers are replaced correctly or ignored

step1:
we want to now find the first missing positive number
iterate thru array in range n:
if nums[i] is not equal to i+1,
return i+1 as the first missing positive interger

Duplicates: Swapping ensures only one valid number stays at each index.
Already sorted input: The scan correctly identifies missing values or returns n + 1.

"""

def firstMissingPositive(nums):

    n = len(nums)
    i = 0

    while i < n:
        correct_idx = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1

#That for loop is scanning from left to right and saying:
#If this number isn't where it should be, then the number that should be here is missing — return that
    for i in range(n):
        if  nums[i] != i + 1:
            return i + 1

    return n + 1

print(firstMissingPositive([1,2,0])) #3
print(firstMissingPositive([3,4,-1,1])) #2
print(firstMissingPositive([7,8,9,11,12])) #1



