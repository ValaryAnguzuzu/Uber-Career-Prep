# You are given an integer array height of length n. There are n vertical lines drawn 
# such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. I
# n this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

#check every possible height

def maxArea(height):
    """
    TC = O(n^2)
    sc = O(1)
    """
    res = 0

    for i in range(len(height)):
        for j in range(i+1, len(height)):
            area = (j - i) * min(height[i], height[j])

            res = max(res, area)
    return res

print(maxArea([1,8,6,2,5,4,8,3,7])) #49
print(maxArea([1,1])) #1

#2 ptrs
#we want to move the ptr that has the min height everytime, to try get a higher area
#traveral ia once as we start from start and another ptr from the end


def maxArea(height):
    """
    TC = O(n)
    sc = O(1)
    """

    l = 0
    r = len(height) - 1
    res = 0

    while l < r:
        area = (r-l) * min(height[l], height[r])

        res = max(area, res)

        #move ptrs accordingly
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return res

print(maxArea([1,8,6,2,5,4,8,3,7])) #49
print(maxArea([1,1])) #1

