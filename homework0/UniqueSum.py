# Given an array of integers, return the sum of unique elements in the array.

def uniqueSum(arr):
    """
    Time Complexity: O(n) - We iterate through the list of numbers once.
    Space Complexity: O(n) - We use a set to store unique nums.
    time - 3 mins
    """

# track unique numns - set()
#iterate
#check if num is not in set - its unique; add it
#return sum

    seen = set()

    for num in arr:
        if num not in seen:
            seen.add(num)

            
    return sum(seen)

print(uniqueSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))  # Expected output: 33
print(uniqueSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6]))  # Expected output: 35

