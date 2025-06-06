# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9


#using 2ptr approach
#we can only trap water when we take min btwn maxLH and maxRH because then water can be contained
#


def trap(height):
        """
        :type height: List[int]
        :rtype: int  
        """
        if not height:
            return 0
        #[0,1,0,2,1,0,1,3,2,1,2,1]
        l = 0
        r = len(height) - 1
        res = 0
        maxLeft = height[l]
        maxRight = height[r]

        while l < r:
            
            #which ptr shld we move
            if maxLeft <= maxRight:
                l += 1
            #check if we can trap water here...
            #get the min to calculate the amt of water trapped
                maxLeft = max(maxLeft, height[l]) 
                res += maxLeft - height[l]

            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]

        return res
print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) #6
print(trap([4,2,0,3,2,5])) #9
