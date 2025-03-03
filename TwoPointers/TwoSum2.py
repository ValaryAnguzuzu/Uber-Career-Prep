# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find 
# two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] 
# and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

 

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

#keep track of num and its index in a dict
#{2:1, 7:2, 11:3, 15:4}

#loop thru the array
#check if target - num in dict
#if yes, return the index of num and index of target - num
#return [index of num, index of target - num] 

            ##this is two sum solution

def twoSum(numbers, target):
    """
    TC = O(N) - we ietaret once
    SC = O(N) - the dict stoarge
    """
    
    num_dict = {}

    for i, num in enumerate(numbers):
        if target - num in num_dict:
            return [num_dict[target - num], i+1]
        num_dict[num] = i+1

# print(twoSum([2,7,11,15], 9)) #[1,2]
# print(twoSum([2,3,4], 6)) #[1,3]
# print(twoSum([-1,0], -1)) #[1,2]


            #two sum2 solution?
#input is sorted
#we can use two pointers
#if l + r > target, decrement r
#if l + r < target, increment l
#if l + r == target, return [l+1, r+1]

def twoSumtwo(numbers, target):
    """
    TC = O(N) - we iterate thru numbers once
    SC= O(1) - no extra space 
    """
    l = 0
    r = len(numbers) - 1

    while l < r:
        if numbers[l] + numbers[r] > target:
            r -= 1

        elif numbers[l] + numbers[r] < target:
            l += 1

        else:
            return [l+1, r+1]

print(twoSumtwo([2,7,11,15], 9)) #[1,2]
print(twoSum([2,3,4], 6)) #[1,3]
print(twoSum([-1,0], -1)) #[1,2]

