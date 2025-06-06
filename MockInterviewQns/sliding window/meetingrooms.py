# Given an array of meeting time intervals where intervals[i] = [start_i, end_i], 
# determine if a person can attend all meetings.

#Input: intervals = [[0,30],[5,10],[15,20]]
#Output: false
# Input: intervals = [[7,10],[2,4]]
# Output: true

#sort intervals by their start time
#if any meeting starts before the prev one ends, return false

def meetingRooms(intervals):
    #sort by their start times
    intervals.sort(key=lambda x:x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < interval[i-1][1]:
            return False
    return True


#Basically return the count of distinct non over lapping intervals
#instead of returning a bool you have to return the greatest count of all valid time slots that the meeting room can hold

#sort by end times
##iterate and if cur interval starts after or when the last selected intravl ends, count it as valid interval

# You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

# You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

# Return the maximum number of events you can attend.



def maxNonOverlappingIntervals(intervals):
    if not intervals:
        return 0
        

    #sort
    intervals.sort(key=lambda x:x[1]) #O(nlog n)

    count = 0
    last_end = float('-inf') #keep track of end time of last added interval

    for start, end in intervals: #O(n)
        if start >= last_end:
            count += 1 #increment count of valid intervals
            last_end = end #update last_end to end of cur interval

    return count

# Example Case 1: General case with overlapping intervals
print(maxNonOverlappingIntervals([[0, 30], [5, 10], [15, 20]]))  # Output: 2

# Example Case 2: Non-overlapping intervals
print(maxNonOverlappingIntervals([[7, 10], [2, 4]]))  # Output: 2

# Example Case 3: Fully overlapping intervals
print(maxNonOverlappingIntervals([[1, 4], [2, 5], [3, 6]]))  # Output: 1

# Example Case 4: Overlapping & non-overlapping mixed
print(maxNonOverlappingIntervals([[1, 3], [2, 4], [3, 5], [4, 6]]))  # Output: 2

# Example Case 5: Completely non-overlapping consecutive intervals
print(maxNonOverlappingIntervals([[1, 2], [2, 3], [3, 4], [4, 5]]))  # Output: 4

# Example Case 6: Single interval
print(maxNonOverlappingIntervals([[1, 5]]))  # Output: 1

# Example Case 7: All intervals have same start time
print(maxNonOverlappingIntervals([[1, 3], [1, 4], [1, 5]]))  # Output: 1

# Example Case 8: Completely overlapping intervals
print(maxNonOverlappingIntervals([[1, 10], [2, 9], [3, 8], [4, 7]]))  # Output: 1

# Example Case 9: Large interval followed by smaller ones
print(maxNonOverlappingIntervals([[1, 10], [11, 12], [12, 13], [13, 14]]))  # Output: 4

# Example Case 10: Edge Case - Empty input
print(maxNonOverlappingIntervals([]))  # Output: 0

# Example Case 11: Single point intervals
print(maxNonOverlappingIntervals([[1, 1], [2, 2], [3, 3]]))  # Output: 3

# Example Case 12: Overlapping intervals that are spread out
print(maxNonOverlappingIntervals([[1, 3], [2, 5], [4, 6], [7, 8]]))  # Output: 3

