'''
Shortest Word Edit Path
Given two words source and target, and a list of words words, find the length of the shortest series of edits that transforms source to target.

Each edit must change exactly one letter at a time, and each intermediate word (and the final target word) must exist in words.

If the task is impossible, return -1.
task 
Examples:
b:1 i:1 t:1
{}
source = "bit", target = "dog"
words = ["dog", "lot", "big", "pot", "pog", "put", "but"]
bit ... 50th word dig 

SPACE: O(n)
TIME: O(v + e)?...look more into this!! --> O(nxq^2) : checking each word in the q
output: 5
explanation: bit -> butter -> put -> pot -> pog -> dog has 5 transitions.
     seen: bit 
   q =  [put, pot, pog] //everything must satisfy condition b4 we add
                        bit
                        /\ diff & length 
                    but.  big
                    /\.     \
                put           .
                /\
            pot.  pog 
            /.      \
        pog.         pot
        /.            \  
    dog                lot
                         \
                          dot
                            \
                              dog 
source = "no", target = "go"
words = ["to"]

output: -1

Constraints:

[time limit] 5000ms
[input] string source
1 ≤ source.length ≤ 20
[input] string target
1 ≤ target.length ≤ 20
[input] array.string words
1 ≤ words.length ≤ 20
[output] array.integer

we only want the transformed word being used once-set
#dict track of freq
{0:[1,1]}
#calculate difference, if its 1 then one letter has changed
#how would i know its the correct answer? ie shortest path -> make sure the diff is always 1 otherwise it means we would have to change more(more edits)

BFS -shortest path
#queue 
#set - track visited
#base case: check diff is always 1; if > 1, we cant use it
check the length of target and source -> miusrt alwyas be equal for us to get to target
we have rea
graph struct :
we dont want to add something to our set that doesnt fully satisfy our condtions 




'''