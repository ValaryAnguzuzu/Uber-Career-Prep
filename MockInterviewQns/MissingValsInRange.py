# Given an array and two integers, lo and hi, defining a range, return the values in the range missing from the array.
# Example
# Input: [8, 12, 18, 11, 15], lo = 7, hi = 16
# Output: [7, 9, 10, 13, 14, 16]



def missing_values_in_range(arr, lo, hi):
    """
    Time Complexity: O(n) - single pass through the array
    space complexity: O(n) - storing the missing values
    """
    # Convert array to a set for O(1) lookups
    arr_set = set(arr)
    # Generate the missing values in the range
    missing_values = [num for num in range(lo, hi + 1) if num not in arr_set]

    return missing_values


def test_missing_values_in_range():
    # Test Case 1: Given example
    assert missing_values_in_range([8, 12, 18, 11, 15], 7, 16) == [7, 9, 10, 13, 14, 16]
    
    # Test Case 2: All numbers are present in range
    assert missing_values_in_range([7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 7, 16) == []
    
    # Test Case 3: No numbers from range are in the array
    assert missing_values_in_range([20, 21, 22], 5, 10) == [5, 6, 7, 8, 9, 10]
    
    # Test Case 4: Single missing number
    assert missing_values_in_range([1, 2, 3, 5, 6], 1, 6) == [4]
    
    # Test Case 5: Array is empty
    assert missing_values_in_range([], 10, 15) == [10, 11, 12, 13, 14, 15]
    
    # Test Case 6: lo == hi and present in array
    assert missing_values_in_range([5], 5, 5) == []
    
    # Test Case 7: lo == hi and missing from array
    assert missing_values_in_range([1, 2, 3, 4], 5, 5) == [5]
    
    # Test Case 8: Large range with sparse array
    assert missing_values_in_range([50, 55, 60, 65], 50, 70) == [
        51, 52, 53, 54, 56, 57, 58, 59, 61, 62, 63, 64, 66, 67, 68, 69, 70
    ]

    print("All test cases passed!")

# Run the test cases
test_missing_values_in_range()
