# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 
# respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored
# inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first
#  m elements denote the elements that should be merged, and the last n elements are set to 
# 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

# Constraints:

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109
 

# Follow up: Can you come up with an algorithm that runs in O(m + n) time?

#iterate simultaneously with 2 ptrs from the end of both arrays
#compare the elements and add the laregr one to the end of nums1
#decrement the ptr of the larger element
#repeat until we have merged all elements from nums2


def MergeSortedArray(nums1, m, nums2, n): #it should also take the lengths of the nums
    """
    TC: O(N+M) - we are iterating thru both strs once
    SC: O(1)
    """
    i = m - 1
    j = n - 1
    k = m + n - 1 #ptr for placement in nums1 

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1

        k -= 1 #once either condition is met, decrement ptr of placement in nums1

        #if nums1 is ever empty, we need to add the remaining elements from nums2
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
        

    return nums1


print(MergeSortedArray([1,2,3,0,0,0], 3, [2,5,6], 3)) #[1,2,2,3,5,6]
print(MergeSortedArray([1], 1, [], 0)) #[1]
print(MergeSortedArray([0], 0, [1], 1)) #[1]
print(MergeSortedArray([4,5,6,0,0,0], 3, [1,2,3], 3)) #[1,2,3,4,5,6]
print(MergeSortedArray([0,0,0,0,0], 0, [5,6,7,8,9], 5))  # Expected output: [5,6,7,8,9]
print(MergeSortedArray([5,6,7,8,9], 5, [0,0,0,0,0], 0))  # Expected output: [5,6,7,8,9]

