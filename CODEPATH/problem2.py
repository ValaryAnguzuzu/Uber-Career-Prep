"""
Problem 2: Pirate Message Check
Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she
 can trust the message if it contains all of the letters in the alphabet. Given a string
 message containing only lowercase English letters and whitespace, write a function can_trust_message() 
 that returns True if the message contains every letter of the English alphabet at least once, and False otherwise.
"""

#run a loop throughout the string
#create a set ad add each element to the set, if its not there
#calculate the len of the set if its 27 return true

#whitespace - 
def can_trust_message(message):
    seen = set()
    #message_two = message.split() #"sphinx of black quartz judge my vow" ["sphinx","of","black","quartz","judge"]
    for c in message:
        #if c not in seen:
            seen.add(c)

    return len(seen) == 27 #we add count for the space



message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1)) #true
print(can_trust_message(message2)) #false
