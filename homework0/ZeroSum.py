#Array & String/Set & Map Problems

# Given an array of integers, return the number of pairs of integers in the array that sum to 0 assuming you can use the element at each index at most once.


def zeroSumPairs(nums):
    """
    :type nums: List[int] - A list of integers
    :rtype: int - The count of unique pairs of integers that sum to zero
    Time Complexity: O(n) - We iterate through the list of numbers once.
    Space Complexity: O(n) - We use a hash map to store frequencies.
    """
#HASHMAP to track occurrences of each num
# initialize var to track count of pairs
#iterate through nums
#compliment = 0 - num
#check if complement exists in map
#if yes, count +1 and decrement complement count; if no, add curr num to map
#return count

# Time Complexity: O(n) - We iterate through the list of numbers once.
# Space Complexity: O(n) - We use a hash map to store frequencies.
    freq = {} 
    count = 0 

    for num in nums:
        complement = -num

        if complement in freq:
            count += 1
            freq[complement] -= 1
        else:
            freq[num] = freq.get(num, 0) + 1
    return count


print(zeroSumPairs([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))  # Expected output: 2
print(zeroSumPairs([1, 10, 8, -2, 2, 5, 7, 2, -2, -1]))  # Expected output: 3
print(zeroSumPairs([4, 3, 3, 5, 7, 0, 2, 3, 8, 6]))      # Expected output: 0
print(zeroSumPairs([4, 3, 3, 5, 7, 0, 2, 3, 8, 0]))   # Expected output: 1


#Now assume you can re-use elements in different pairs (i.e., the elements in a pair must be from different indices but different pairs may use an element form the same index).
# Examples:
# Input Array: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
# Output: 3
# (Pairs: (1, -1), (2,-2), (2,-2))

# Input Array: [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
# Output: 5
# (Pairs: (1, -1), (2,-2), (2,-2), (2,-2), (2,-2))

# Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
# Output: 0

# Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]
# Output: 1
# (Pairs: (0, 0))

# def zeroSumPairsR(nums):
#     """
#     :type nums: List[int] - Input array of integers
#     :rtype: int - The count of zero-sum pairs
#     """
# #hash map to count frequencies
# #iterate over keys in freq to find pairs
# #if complement exists, num of pairs that can be formed is min of both frequencies; increment pairs count

#     freq = {}
#     count = 0

#     for num in nums:
#         freq[num] = freq.get(num, 0) + 1

#     for num in list(freq.keys()):
#         complement = -num
#         if complement in freq:
#             pairs = min(freq[num], freq[complement])
#             count += pairs
        
#     return count

# print(zeroSumPairsR([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))  # Expected output: 3; (Pairs: (1, -1), (2,-2), (2,-2))


#time taken - 40+ mins

#NEW ATTEMPT!
#keep track of already visited elements before the cur element
def zeroSumFollowUp(nums):
    """
    time complexity - O(n)
    space complexity - O(n) 
    5 mins
    """
    count = 0 
    freq = {}

    for num in nums:
# once we get the complement of the current element, let's add all the possible pairs with the already visited numbers

        if -num in freq:
            count += freq[-num] #updating count with the num of occurences of -num 
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    return count

print(zeroSumFollowUp([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))  # Expected output: 3; (Pairs: (1, -1), (2,-2), (2,-2))
print(zeroSumFollowUp([])) # 0 pairs expected
print(zeroSumFollowUp([1])) # 0 pairs expected
print(zeroSumFollowUp([-1, -3, -5, -6])) # 0 pairs expected
print(zeroSumFollowUp([0, 0, 0, 0])) # 6 pairs expected
print(zeroSumFollowUp([1, 10, 8, 3, 2, 5, 7, 2, -2, -1])) # 3 pairs expected
print(zeroSumFollowUp([1, 10, 8, -2, 2, 5, 7, 2, -2, -1])) # 5 pairs expected
print(zeroSumFollowUp([4, 3, 3, 5, 7, 0, 2, 3, 8, 6])) # 0 pairs expected
print(zeroSumFollowUp([4, 3, 3, 5, 7, 0, 2, 3, 8, 0])) # 1 pair expected
