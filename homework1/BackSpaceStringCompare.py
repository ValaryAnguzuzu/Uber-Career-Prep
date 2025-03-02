# Question 4: BackspaceStringCompare
# Given two strings representing series of keystrokes, 
# determine whether the resulting text is the same. Backspaces are 
# represented by the '#' character so "x#" results in the empty string ("").

# Examples:
# eInput Strings: "abcde", "abcde"
# Output: True

# Input Strings: "Uber Career Prep", "u#Uber Careee#r Prep"
# Output: True

# Input Strings: "abcdef###xyz", "abcw#xyz"
# Output: True

# Input Strings: "abcdef###xyz", "abcdefxyz###"
# Output: False

#if there is no # return true
#2 stacks
#if # pop from stack; check its nonepty first, else push to stack
#compare the two stacks

def BackspaceStringCompare(s, t):
    """
    technique: Stack
    time complexity is O(n+m) because we are iterating through both strings
    space complexity is O(n) because we are storing the strings in a stack
    time taken: 10mins
    """
    stackS = []
    stackT = []

    for char in s:
        if char == '#':
            if stackS:
                stackS.pop()
        else:
            stackS.append(char)

    for char in t:
        if char == '#':
            if stackT:
                stackT.pop()
        else:
            stackT.append(char)

    return stackS == stackT

print(BackspaceStringCompare("abcde", "abcde")) #True
print(BackspaceStringCompare("Uber Career Prep", "u#Uber Careee#r Prep")) #True
print(BackspaceStringCompare("abcdef###xyz", "abcw#xyz")) #True
print(BackspaceStringCompare("abcdef###xyz", "abcdefxyz###")) #False
print(BackspaceStringCompare("a##c", "#a#c")) #True


#OFFICE HOURS: two pointers is the BETTER approach for this question

    

