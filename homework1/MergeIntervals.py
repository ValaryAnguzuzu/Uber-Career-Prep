"""Question 8: MergeIntervals
Given a list of integer pairs representing the low and high end of an interval, inclusive, return 
a list in which overlapping intervals are merged.

Examples:

Input: [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
Output: [(4, 8), (1, 3), (9, 12)]

Input: [(5, 8), (6, 10), (2, 4), (3, 6)]
Output: [(2, 10)]

Input: [(10, 12), (5, 6), (7, 9), (1, 3)]
Output: [(10, 12), (5, 6), (7, 9), (1, 3)]

"""


#if we can sort, we can bring overlapping intevals close together: we would then process intervals in order, so merging becomes easier.
#we then can keep track of the prev interval so that if the next interval starts before the prev ends, we can merge them
#we can use two pointers to keep track of the start and end of the interval
#we can then append the merged interval to the result list
#we can then return the result list

    #sorted: [(1, 2), (2, 3), (4, 8), (5, 7), (9, 12)]
    #merged: [(1, 3) , (4, 8), (5, 7), (9, 12)]

def merge_intervals(intervals):
    """
    technique: Sorting & Searching - Sort the Array, Then Solve
    time complexity: O(nlogn) - sorting dominated here
    space complexity: O(n) - storing the merged intervals
    time taken: 50 mins - It took me a while to make implement the working solution
    """
    if not intervals:
    
        return []

    intervals.sort() #sorts by the first val in each tuple
    merged = [intervals[0]] #start with the first interval

    #iterate thru the remaining intervals
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1] #Get the last merged interval

        if start <= last_end: #there is an aoverlap
            merged[-1] = (last_start, max(last_end, end)) #so merge them with the high of cur interval being the new end


        else:
            merged.append((start, end)) #add separately, they dont iverlap

    return merged

# Provided test cases:
print(merge_intervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)])) #[(4, 8), (1, 3), (9, 12)]

print(merge_intervals([(5, 8), (6, 10), (2, 4), (3, 6)])) # [(2, 10)]
print(merge_intervals([(10, 12), (5, 6), (7, 9), (1, 3)])) # [(1, 3), (5, 6), (7, 9), (10, 12)]






