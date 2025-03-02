# Question 9: DedupArray
# Given a sorted array of non-negative integers, modify the array by removing 
# duplicates so each element only appears once. If arrays are static (aka, not dynamic/resizable)
#  in your language of choice, the remaining elements should appear in the left-hand side of 
# the array and the extra space in the right-hand side should be padded with -1s.

# Examples:
# Input Array: [1, 2, 2, 3, 3, 3, 4, 4, 4, 4] [1, 2, 2, 3, 4]
# Modified Array: [1, 2, 3, 4] 
# or [1, 2, 3, 4, -1, -1, -1, -1, -1, -1] (depending on language)

# Input Array: [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
# Modified Array: [0, 1, 4, 5, 8, 9, 10, 11, 15]
# or [0, 1, 4, 5, 8, 9, 10, 11, 15, -1, -1, -1, -1, -1] (depending on language)

# Input Array: [1, 3, 4, 8, 10, 12]
# Modified Array: [1, 3, 4, 8, 10, 12]

#loop from the end, 
#remove the arr[i] if its == to arr[i-1] and move pointer to the left if not just move the ptr
#if not, then replace the arr[i] with arr[i+1]

def DedupArray(arr):
    """
    Time complexity = O(n^2)
    Space complexity = O(1)
    time = 30mins
    I took this like a normal interview; tok me the 25mins to come up with this brute force sln which I think 
    we can do better. I will try to come up with a better sln below this

    [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15])) - this test case failed at first -> [0, 0, 1, 4, 5, 8, 9, 10, 11, 15] 
        so i changed while loop to  while i >= 0 instead of while i > 0: and it worked
    """
    i = len(arr) - 2
    while i >= 0:
        if arr[i] == arr[i-1]:
            if arr[i] == arr[i+1]:
                arr.remove(arr[i])
            i -= 1
        else:
            if arr[i] == arr[i+1]:
                arr.remove(arr[i])
            i -= 1
    return arr
        
print(DedupArray([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])) #[1, 2, 3, 4]
print(DedupArray([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15])) #[0, 1, 4, 5, 8, 9, 10, 11, 15]




#CAN WE DO BETTER?

#l and r, l keeps track of positions to replace and r traverses

def DedupArray(arr):
    """
    technique: two pointers
    time complexity = O(n) - one pass through the array
    space complexity = O(1) - in place modification
    time = 10mins
    """
    l = 1


    for r in range(1, len(arr)):
        if arr[r] != arr[r-1]:
            arr[l] = arr[r]
            l += 1
    return arr[:l]

print(DedupArray([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])) #[1, 2, 3, 4]
print(DedupArray([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15])) #[0, 1, 4, 5, 8, 9, 10, 11, 15]
print(DedupArray([1, 3, 4, 8, 10, 12])) #[1, 3, 4, 8, 10, 12]
print(DedupArray([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) #[1]
print(DedupArray([1, 1, 1, 1, 1, 1, 1, 1, 1, 2])) #[1, 2]
print(DedupArray([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2,5,5,5])) #[1, 2, 5]
