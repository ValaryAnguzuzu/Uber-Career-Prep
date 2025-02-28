"""Question 6: MissingInteger
Given an integer n and a sorted array of integers of size n-1 which contains all but one of the integers in the range 1-n, find the missing integer.

Examples:
Input Array: [1, 2, 3, 4, 6, 7]
Input n: 7
Output: 5

Input Array: [1]
Input n: 2
Output: 2

Input Array: [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
Input n: 12
Output: 9

"""

#we can iterate thru the range 1: n and for each iteration check if i is in our input arr...which we can convert to a set for easy lookup
#our sc would be O(n) tc is O(n) too


#but we can do better...we can use binary search
#because input arr is sorted - > binary search?
#we can check if the midpoint is equal to the midpoint + 1 eg
    # Index:   0   1   2   3   4   5   6 here at arr[i] the val is i + 1
    # Value:   1   2   3   4   5   6   7 so it emeans whenever this pattern breaks , the idx that breaks this. its val is our ans
    # we can use binary search to find the idx that breaks this pattern
#missing num will always be l +1 if mid + 1 != arr[mid] -- break point 


def missingInteger(arr, k):
    """
    Technique: Sorting & Searching: Binary search variation
    Time Complexity: O(log n) - binary search
    Space Complexity: O(1)
    Time Taken: 30 minutes

    I was able to note at first that this needs binary search!! nice
    I took some time to figure out the trick \ that the missing number will always be l + 1 if mid + 1 != arr[mid]
    """
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        expected_value = mid + 1

        if arr[mid] == expected_value:
            l = mid + 1 #search right because this means so far the left has not broken the pattern
        else:
            r = mid - 1

    return l + 1 

# Provided test cases:
print(missingInteger([1, 2, 3, 4, 6, 7], 7)) # expected: 5
print(missingInteger([1], 2)) # expected: 2
print(missingInteger([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12)) # expected: 9
