"""
A game where a charcter moves through a level

if character collects a coin player scores a point.
if the segment does not contain a coin the player loses a point
player 1 always begins
at some point game is turned to player 2 to complete the level
player 1 tries to achieve a higher score than player 2 once the level is completed

given status of game segments, determine minimum number of segments player 1 should play so that his score is greater than player 2

Example:
[1,1,0,1]
0 segments -->  Player 1: 0     Player 2: 2
1 segment --> Player 1: 1       Player 2: 1
2 segments --> Player 1: 2      Player 2: 0

GET MINIMUM

input: array of segments (each segment can only have 1 coin)
output: int (no of segments)

[1,1,1,1,1] == 3
[1,0,1,1,1] == 4
[1,1,1,1,0] == 2

[1,1,1,1,1] --> 

pseudocode
sum up the total score = 3
threshold = 3/2 = 2  --> for player1 ro win they must get more than half of the possible points
keep track of player1's sum = 2
for i in nums
if nums[i] == 1: sum += 1
else: sum -=1
check against threshold, if >, break 
return index

([1,1,0,1,1])) 
tota number of items = len(arr) == 5
number of ones = sum(arr) == 4
number of zeros = total number of items - sum(arr) == 5 -4 == 1
actual points = numnber of ones - number of zeros === 4 - 1 == 3
"""

def playSegments(coins):
    #edge cases:[all 0] player1 DONT play


    total_sum = sum(coins)#total number of ones -->, 4
    n = len(coins)#number of items(1/0) --> 5
    zeros = n - total_sum #number of zeros which cancel out the same number of 1's --> 1
    total_points = total_sum - zeros # --> 3
     

    score = 0
    threshold = total_points / 2 #1.5

    for i in range(len(coins)):
        if coins[i] == 1:
            score += coins[i]
        else:
            score -= 1

        if score > threshold:
            break

    return i + 1
#i = 0, 1
#score = 2
print(playSegments([1,1,0,1])) #2
print(playSegments([1,1,1,1,1])) #3
print(playSegments([1,1,0,1,1])) #4
print(playSegments([1,1,1,1,0])) #2
print(playSegments([1,1,1,1])) #3


"""
def playSegments(coins):
    n = len(coins)

    for p1_segments in range(1, n):
        p1_score = 0
        for i in range(p1_segments):
            if coins[i] == 1:
                p1_score += 1
            else:
                p1_score -= 1

        p2_score = 0
        for i in range(p1_segments, n):
            if coins[i] == 1:
                p2_score += 1
            else:
                p2_score -= 1

        if p1_score > p2_score:
            return p1_segments

    return -1

# Test cases
print(playSegments([1, 1, 0, 1]))  # Expected: 2
print(playSegments([1, 1, 1, 1, 1]))  # Expected: 3
print(playSegments([1, 0, 1, 1, 1]))  # Expected: 4
print(playSegments([1, 1, 1, 1, 0]))  # Expected: 2
print(playSegments([1, 1, 1, 1])) # Expected: 3
print(playSegments([0, 0, 0])) # Expected: -1





def playSegmentsLinear(coins):
    n = len(coins)
    total_p2_score = 0
    for coin in coins:
        if coin == 1:
            total_p2_score += 1
        else:
            total_p2_score -= 1

    p1_score = 0
    for p1_segments in range(1, n):
        if coins[p1_segments - 1] == 1:
            p1_score += 1
            total_p2_score -= 1  # Player 1 takes a coin, reducing P2's potential
        else:
            p1_score -= 1
            total_p2_score += 1  # Player 1 takes an empty, increasing P2's potential

        if p1_score > total_p2_score:
            return p1_segments

    return -1

# Test cases
print(playSegmentsLinear([1, 1, 0, 1]))    # Expected: 2
print(playSegmentsLinear([1, 1, 1, 1, 1]))    # Expected: 3
print(playSegmentsLinear([1, 0, 1, 1, 1]))    # Expected: 4
print(playSegmentsLinear([1, 1, 1, 1, 0]))    # Expected: 2
print(playSegmentsLinear([1, 1, 1, 1]))   # Expected: 3
print(playSegmentsLinear([0, 0, 0]))    # Expected: -1
    
"""