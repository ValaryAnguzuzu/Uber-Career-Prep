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

# print(BackspaceStringCompare("abcde", "abcde")) #True
# print(BackspaceStringCompare("Uber Career Prep", "u#Uber Careee#r Prep")) #True
# print(BackspaceStringCompare("abcdef###xyz", "abcw#xyz")) #True
# print(BackspaceStringCompare("abcdef###xyz", "abcdefxyz###")) #False
# print(BackspaceStringCompare("a##c", "#a#c")) #True


#OFFICE HOURS: two pointers is the BETTER approach for this question

    
#s= "abcdef###xyz", t = "abcw#xyz")
#back_s = 3  back_t = 1
def backspace(s, t):
    l = len(s) - 1
    r = len(t)- 1 #we start at he end of both strs
    back_s = 0
    back_t = 0 #count backsaces we find

    while l >= 0 or r >= 0:  #this, because the idea is we want to process both strs simultaneously!!!

    
        #s
        while l >= 0:
            if s[l] == "#":
                back_s += 1
                l -= 1

        
            elif back_s > 0: #its not a backspace but we have seen backspaces before; ,meaning, we need to delete or skip this char
                back_s -= 1    #ie   def### -> back_s = 3, so we reduce it when we find f, d, and e
                l -= 1

            else:
                #l -= 1  we want to break, so that we move to comparing the chars at this stage.... before we move ptrs
                break
        #t
        while r >= 0:
            if s[r] == "#":
                back_t += 1
                r -= 1

        
            elif back_t > 0:
                back_t -= 1
                r -= 1

            else:
                #r -= 1     we want to break, so that we move to comparing the chars at this stage.... before we move ptrs
                break

        #compare if both are still valid
        if l >= 0 and r >= 0 and s[l] != t[r]:  #after executing else and breaking from both strs, w copare the curr chars
            return False

        l -= 1 #now that we have compared and theyre similar, so we can move our ptrs 
        r -= 1
    return True # all chars matched
        

print(BackspaceStringCompare("abcde", "abcde")) #True
print(BackspaceStringCompare("Uber Career Prep", "u#Uber Careee#r Prep")) #True
print(BackspaceStringCompare("abcdef###xyz", "abcw#xyz")) #True
print(BackspaceStringCompare("abcdef###xyz", "abcdefxyz###")) #False
print(BackspaceStringCompare("a##c", "#a#c")) #True

