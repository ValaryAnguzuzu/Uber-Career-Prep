# Given an array and an integer k, return the first element that occurs k times
# input: [2, 2, 3, 4, 5, 7, 7, 7, 9, 9], k = 2
# output: 2

from collections import defaultdict

def first_element_k_times(arr, k):
    freq = defaultdict(int)
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] == k:
            return num


def test_first_element_k_times():
    # Test Case 1: Given example
    assert first_element_k_times([2, 2, 3, 4, 5, 7, 7, 7, 9, 9], 2) == 2

    # Test Case 2: First element occurring k times is in the middle
    assert first_element_k_times([1, 3, 3, 5, 5, 5, 7, 7], 3) == 5

    # Test Case 3: Only one element in array occurring k times
    assert first_element_k_times([4, 4, 4, 4], 4) == 4

    # Test Case 4: k is greater than the occurrences of any element
    assert first_element_k_times([1, 2, 3, 4], 2) is None  # No element appears twice

    # Test Case 5: The first element appearing k times is at the beginning
    assert first_element_k_times([5, 5, 6, 7, 8, 8, 9, 9, 9], 2) == 5

    print("All test cases for first_element_k_times passed!")

#FOLLOW UP

# Given an array and an integer k, return the last element that occurs k times
# input: [2, 2, 3, 4, 5, 7, 7, 7, 9, 9], k = 2
# output: 9


def last_element_k_times(arr, k):
    freq = defaultdict(int)
    # Traverse the array in reverse
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        freq[num] = freq.get(num, 0) + 1
        if freq[num] == k:
            return num


def test_last_element_k_times():
    # Test Case 1: Given example
    assert last_element_k_times([2, 2, 3, 4, 5, 7, 7, 7, 9, 9], 2) == 9

    # Test Case 2: Last element occurring k times is in the middle
    assert last_element_k_times([1, 3, 3, 5, 5, 5, 7, 7], 3) == 5

    # Test Case 3: Only one element in array occurring k times
    assert last_element_k_times([4, 4, 4, 4], 4) == 4

    # Test Case 4: k is greater than the occurrences of any element
    assert last_element_k_times([1, 2, 3, 4], 2) is None  # No element appears twice

    # Test Case 5: The last element appearing k times is at the end
    assert last_element_k_times([5, 5, 6, 7, 8, 8, 9, 9, 9], 2) == 9

    print("All test cases for last_element_k_times passed!")


# Run the test cases
test_first_element_k_times()
test_last_element_k_times()