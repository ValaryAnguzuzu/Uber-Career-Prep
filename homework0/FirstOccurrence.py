def firstOccurrence(s):
    """
    :type s: str - input String
    :rtype: str - A string with only the first occurrence of each character
    Time Complexity: O(n) - We iterate through the list of numbers once.
    Space Complexity: O(n) - We use a set to store seen characters and a list for the result.
    time - 10 mins
    """
#track seen characters - set()
# a alist to store result
#iterate
#  if char is not in seen, add it to seen for tracking aand to result
# return result as a string 

    seen = set()
    result = []
    for char in s:
        if char not in seen:
            result.append(char)
            seen.add(char)
    return ''.join(result)

print(firstOccurrence("abracadabra"))  # Expected output: "abrcd"
print(firstOccurrence("Uber Career Prep"))  # Expected output: "Uber CaPp"
print(firstOccurrence("zzyzx"))  # Expected output: "zyx"


