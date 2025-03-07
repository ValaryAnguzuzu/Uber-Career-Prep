# You are given an array people where people[i] is the weight of the ith person, 
# and an infinite number of boats where each boat can carry a maximum weight of limit.
#  Each boat carries at most two people at the same time, provided the sum of the 
# weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.

 

# Example 1:

# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# Example 2:

# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# Example 3:

# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)


#if we sort our input, w are guaranteed the heavier person will alwys be in a boat, then we can check for the lightest from left
        #to se if we can add a lightest psn or not
def numRescueBoats(people, limit):
    """
    TC= O(nlogn)
    SC = O(1)
    """
    people.sort()
    boats = 0
    l = 0
    r = len(people) - 1

    while l <= r: #= checks whethr we have one psn left ta the end 
        remain = limit - people[r] #how much more space or weight we can take in a boat

        r -= 1 #since prople[r], the heaviest will alwyas have  a boat, move to the next psn
        boats += 1 #increment num of boats

        #but, still check, can the lightest psn fit in the same boat above?

        if l <= r and people[l] <= remain: #can only fit if they are less or equal to our remaiing space/capacity
            l += 1 #means they can be added...so move to the next

    return boats

print(numRescueBoats([1, 2], 3)) #1
print(numRescueBoats([3,2,2,1], 3)) #3
print(numRescueBoats([3,5,3,4], 5)) #4

