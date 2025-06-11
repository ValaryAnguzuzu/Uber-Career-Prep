"""
Booby Trap
Captain Feathersword has found another pirate's buried treasure, but they suspect it's booby-trapped. 
The treasure chest has a secret code written in pirate language, and Captain Feathersword believes the 
trap can be disarmed if the code can be balanced. A balanced code is one where the frequency of every letter 
present in the code is equal. To disable the trap, Captain Feathersword must remove exactly one letter from the 
message. Help Captain Feathersword determine if it's possible to remove one letter to balance the pirate code.

Given a 0-indexed string code consisting of only lowercase English letters, write a function is_balanced() that
 returns True if it's possible to remove one letter so that the frequency of all remaining letters is equal, and 
 False otherwise.
"""
# do we consider spaces?
# if the code is empty? return false?
# dict to store the freqs of each of the characters -
# how do we keep track of when if decrease count of one character the rest are still equal
#
# store all the frq values to a set - does not allow duplictes?
#{a:1, r:1, g:1, h:2} -> set = {1, 2} -> 2-1 = 1 add 1 to the set = {1}
# {a:1, r:1, g:1, h:2, z:3} -> set={1,2,3} -> 3-1 = 2 add 2 to the set = {1,2}
# {h:2, a: 2} -> set = {2} => IF SET IS ALREADY BALANCED - HAS ONE ELT, RETURN FALSE

def is_balanced(code):
    freq = dict()
    seen = set()

    for c in code:
        freq[c] = freq.get(c, 0) + 1
    
    seen = freq.values()
    print(seen)

code1 = "arghh" 
code2 = "haha"
code3 = "arghhzzz"

print(is_balanced(code1)) 
# print(is_balanced(code2)) 