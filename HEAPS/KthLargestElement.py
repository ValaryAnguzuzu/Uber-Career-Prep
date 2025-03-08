import heapq
# You are part of a university admissions office and need to keep track of the kth highest test 
# score from applicants in real-time. This helps to determine cut-off marks for interviews and 
# admissions dynamically as new applicants submit their scores.

# You are tasked to implement a class which, for a given integer k, maintains a stream of test 
# scores and continuously returns the kth highest test score after a new score has been submitted.
# More specifically, we are looking for the kth highest score in the sorted list of all scores.

# Implement the KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
# int add(int val) Adds a new test score val to the stream and returns the element representing the kth 
# argest element in the pool of test scores so far.
 

# Example 1:

# Input:
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

# Output: [null, 4, 5, 5, 8, 8]

# Explanation:

# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3); // return 4  [8,5,4,3,2]
# kthLargest.add(5); // return 5 [8,5, 5,4, 3,2,]
# kthLargest.add(10); // return 5
# kthLargest.add(9); // return 8
# kthLargest.add(4); // return 8

# Example 2:

# Input:
# ["KthLargest", "add", "add", "add", "add"]
# [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

# Output: [null, 7, 7, 7, 8]

# Explanation:

# KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
# kthLargest.add(2); // return 7 [8, 7 7 7 7 7 3 2]
# kthLargest.add(10); // return 7
# kthLargest.add(9); // return 7
# kthLargest.add(9); // return 8

#we want to only keep the k elements in our heap, so for every incoming, check if its greater than
#curr kth largest which is always at idx 0 or if the length is still < k
#if one of this is true, 
class KthLargest:
    def __init__(self, k, nums):
        #input: k and arr of nums
        self.largest = []
        self.k = k
        for num in nums:
            self.add(num)
        # heapq.heapify(self.largest)
        # for element in arr:
        #     heapq.heappush(self.largest, element)
        # self.largest = heapq.heapify(arr)
        

    def add(self, val): # [4,5,8] k = 3
        #input: val beign added
        #output: the kth largest value
        if len(self.largest) < self.k or val > self.largest[0]:
            heapq.heappush(self.largest, val)
            if len(self.largest) > self.k:
                heapq.heappop(self.largest)
        
        return self.largest[0]





# initialize a heap using the heapq module, which provides a min-heap by default.
# import heapq

# heap = []  # Create an empty list to use as a heap
# # heapq.heapify(heap)  # Convert the list into a valid heap (though it's already empty)

# heapq.heappush(arr, 5)
# heapq.heappush(heap, 1)
# heapq.heappush(heap, 3)



# Good question! Python’s heapq module only provides a min-heap, but you can simulate a max-heap using negation.

# How nlargest() Works in a Min-Heap
# Even though heapq only supports min-heaps, functions like heapq.nlargest() and heapq.nsmallest() do not require the 
# heap to be explicitly a max-heap or min-heap beforehand. Instead, they work by:

# Building a heap internally from the given iterable.
# Extracting the n largest or smallest elements efficiently.
# Example: Using heapq.nlargest() in a Min-Heap

# import heapq

# nums = [4, 7, 1, 9, 2]

# # Get the 2 largest elements
# largest_two = heapq.nlargest(2, nums)
# print(largest_two)  # Output: [9, 7]

# # Get the 3 smallest elements
# smallest_three = heapq.nsmallest(3, nums)
# print(smallest_three)  # Output: [1, 2, 4]
# How does heapq.nlargest() work?

# Instead of maintaining a full heap, it keeps a temporary min-heap of size n.
# It iterates through the data, keeping only the n largest elements in memory.
# This makes it more efficient than sorting the entire list and slicing.
# Simulating a Max-Heap for Priority Queues
# If you want an actual max-heap behavior (where the largest element is always at the root), you can negate values 
# when inserting and retrieving elements:

# python
# Copy
# Edit
# max_heap = []
# heapq.heappush(max_heap, -5)
# heapq.heappush(max_heap, -1)
# heapq.heappush(max_heap, -3)

# print(-heapq.heappop(max_heap))  # Output: 5 (largest element)




"""
NOTE 
#HEAPS
#Mainly used to implement a priority queue 
A PQ: Is a ordered queue and they areordered according priority (smallest or largest mostly)


import heapq

nums = [5,6,1,2,3,4,4,5]
heapq.heapify(nums) #converts a list or any iteerable into a heap or priority queue
print(nums)#HEAPIFY is the process of converting alist to a heap-ordered list(where the nums[0] is the smallest element and the child is always greater than the parent)

#heappush(heap, ele): This function is used to insert the element mentioned in its arguments into a heap. The order is adjusted, so that heap structure is maintained.
#heappop(heap): This function is used to remove and return the smallest element from the heap. The order is adjusted, so that heap structure is maintained.#
heapq.heappush(nums, 0)
print(nums)  # Output: [0, 2, 1, 5, 4, 3]
smallest = heapq.heappop(nums)
print(smallest)  # Output: 0
print(nums)      # Output: [1, 2, 3, 4, 5]

#Replace the smallest element with a new value and adjust the heap:
heapq.heapreplace(nums, 6)
print(nums)  # Output: [2, 4, 3, 5, 6]


#Python’s heapq module only supports a min-heap. 
# To create a max-heap, you can invert the values by multiplying them by -1 when inserting or removing elements.

#You can use heapq to efficiently find the smallest or largest elements in a list.
#using nsmallest and nlargest
nums = [7, 10, 4, 3, 20, 15]
k = 3
print(heapq.nsmallest(k, nums))  # Output: [3, 4, 7]
print(heapq.nlargest(k, nums))  # Output: [20, 15, 10]


#Efficiently merge multiple sorted lists into a single sorted list using heapq.merge
a = [1, 3, 5]
b = [2, 4, 6]
print(list(heapq.merge(a, b)))  # Output: [1, 2, 3, 4, 5, 6]

#summary
heapq.heapify(list) makes a list a min-heap based on priority values --O(N)
    heapq.heapify(nums)
heapq.heappush(nums, ele) pushes the element to the heap nums O(log N)
    nums = [1, 2, 3]
    heapq.heappush(nums, 0)
    print(nums)  # Output: [0, 1, 3, 2]
heapq.heappop() removes the smallest element from heap O(log N)
    nums = [1, 2, 3]
    heapq.heapify(nums)
    smallest = heapq.heappop(nums)
    print(smallest)  # Output: 1
    print(nums)      # Output: [2, 3]
heapq.heapreplace(nums, ele) Pop and return smallest, and push ele onto the heap  O(log N)
    heapq.heapreplace(nums, 4)
heapq.nsmallest(k, list) Return the k smallest elements O(log N)
    nums = [7, 10, 4, 3, 20, 15]
    k_smallest = heapq.nsmallest(3, nums)
    print(k_smallest)  # Output: [3, 4, 7]
heapq.nlargest(k, list) Return the k largest elements O(k log N)
    nums = [7, 10, 4, 3, 20, 15]
    k_largest = heapq.nlargest(3, nums)
    print(k_largest)  # Output: [20, 15, 10]
heapq.merge(sortedlist1, sortedlist2) Efficiently merge multiple sorted lists into a single sorted list O(k log N)
    a = [1, 3, 5]
    b = [2, 4, 6]
    merged = list(heapq.merge(a, b))
    print(merged)  # Output: [1, 2, 3, 4, 5, 6]




"""

    

""""""