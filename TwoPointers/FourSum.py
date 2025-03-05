# Given an array nums of n integers, return an array of all the unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0     [-2,-1,0,0,1,2]
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]


#sort the arr - for dup handling and 2 ptr approach to work
#recursive function to reduce the ksum
#base case is k ==2 so 2sum with two ptrs


def fourSum(nums, target):
    #sort
    nums.sort()
    res = []
    quad = []

    #recursive func;  handle base case first
    def kSum(k, start, target):
        if k == 2: #base case; 2ptrs
            l = start
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1 #check for more unique elements
                    r -= 1

                    #but we want to avoid repetition
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
            return
        

        #if k !=2, do call ksum
        for i in range(start, len(nums) - k + 1):#this ensures we have enough elements left; ie atleast k numbers left
            #avoid dups for first num a

            if i > start and nums[i] == nums[i-1]:
                continue
            quad.append(nums[i])

            kSum(k-1, i+1, target-nums[i])
            quad.pop() #remove the last added element before exploring new possibilities- essential part of backtracking, ensuring that every combination is unique

    kSum(4, 0, target)

    return res


print(fourSum([1, 0, -1, 0, -2, 2], 0))  # Expected output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(fourSum([2, 2, 2, 2, 2], 8))        # Expected output: [[2,2,2,2]]

