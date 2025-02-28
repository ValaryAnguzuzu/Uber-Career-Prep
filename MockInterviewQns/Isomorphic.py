# Two strings are considered isomorphic if the characters in one string
#  can be replaced to get the characters in the other string. No two distinct 
# characters can be replaced by the same character, but a character can be replaced with itself
# Two dictionaries to track character mappings.
# Iterate through both strings simultaneously
# Ensuring one-to-one mapping
#    - If a character from s1 was mapped to multiple characters in s2, return False and Vice versa
#  Otherwise true


def is_isomorphic(s1, s2):
    """
    Time Complexity: O(n) - single pass through the strings
    space Complexity: O(n) - storing the mappings
    """
    if len(s1) != len(s2):
        return False  # Strings must be the same length

    map_s1 = {}  # Mapping from s1 → s2
    map_s2 = {}  # Mapping from s2 → s1
    for i in range(len(s1)):
        char1, char2 = s1[i], s2[i]
        # If char1 is already mapped, ensure consistency
        if char1 in map_s1:
            if map_s1[char1] != char2:
                return False
        else:
            map_s1[char1] = char2
        # If char2 is already mapped, ensure consistency
        if char2 in map_s2:
            if map_s2[char2] != char1:
                return False
        else:
            map_s2[char2] = char1
    return True

# Test cases
print(is_isomorphic("egg", "add"))  # True
print(is_isomorphic("foo", "bar"))  # False
print(is_isomorphic("paper", "title"))  # True
print(is_isomorphic("badc", "baba"))  # False
