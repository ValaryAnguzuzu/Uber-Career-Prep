"""Problem 1: Arrange Guest Arrival Order
You are organizing a prestigious event, and you must arrange the order in which guests arrive based on their status. The sequence is dictated by a 0-indexed string arrival_pattern of length n, consisting of the characters 'I' meaning the next guest should have a higher status than the previous one, and 'D' meaning the next guest should have a lower status than the previous one.

You need to create a 0-indexed string guest_order of length n + 1 that satisfies the following conditions:

guest_order consists of the digits '1' to '9', where each digit represents the guest's status and is used at most once.
If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].
Return the lexicographically smallest possible string guest_order that meets the conditions.

def arrange_guest_arrival_order(arrival_pattern):
  pass
Example Usage:

print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  
Example Output:

123549876
4321

"""
#use a stack and an ooutput list
#so anytime we see a D, push to the stack BUT anytime we see an I, PUSH THEN POP FROM everything from THE STACK
#Also,  when we reach to the end of the input, pop everything from the stack

def arrange_guest_arrival_order(arrival_pattern):
  result = []
  stack = []

  for i in range(len(arrival_pattern) + 1):
    stack.append(i+1)

  # If pattern[i] is 'I' or we're at the end, pop stack
    if i == len(arrival_pattern) or arrival_pattern[i] == "I":
      while stack:
        result.append(stack.pop())

  return result


print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  


