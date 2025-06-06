#Basically return the count of distinct non over lapping intervals
#instead of returning a bool you have to return the greatest count of all valid time slots that the meeting room can hold

#sort by end times
##iterate and if cur interval starts after or when the last selected intravl ends, count it as valid interval

# You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

# You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

# Return the maximum number of events you can attend.



def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        if not events:
            return 0