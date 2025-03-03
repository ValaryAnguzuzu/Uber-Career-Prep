# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
#  i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.



def threeSumBruteForce(nums):
    """
    TC= O(N^3) - three nested loops
    SC= O(n) -set for removing duplicates
    """

    result = set()

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add(tuple(sorted([nums[i], nums[j], nums[k]])))

    return list(result)

print(threeSumBruteForce([-1, 0, 1, 2, -1, -4]))  # Expected output: [[-1, -1, 2], [-1, 0, 1]]
print(threeSumBruteForce([0,1,1]))  # Expected output: []
print(threeSumBruteForce([0,0,0]))  # Expected output: [[0,0,0]]

        #####BETTER?
# we can sort and think of twosum2...then use it to achieve three sum