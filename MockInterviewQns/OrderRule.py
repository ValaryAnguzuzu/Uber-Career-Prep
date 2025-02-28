# Verify whether a long text is following the order rule defined in 
# order string. For example the order string is "abcd", which means "a"
#  can't appear at any position after "b", "c" and "d" in the text, "b" 
# can't appear at any position after "c" and "d" in the text and "c" can't 
# appear at any position after "d" in the text. if the text is "axubbxcxbxd", 
# then the text didn't follow the rule, since "b" appears after "c" in substring "cxb".


#we want to keep track of the order of the characters in the order string
#we can use a dictionary to keep track of the order of the characters; key is the character and
#  value is the index as is in order
#we can then iterate through the text and check if the order of the characters is maintained
#init max seen index to -1; update it to the index of the character in the order string

#at each iteration, we check if the index of the character in the order string is greater than the max seen index
# if it is not, we return False, order has been violated

#after the loop, we return True, order has been maintained

def orderRule(order, text):
    """
    Technique: Hashing; hashmap
    Building the order_map dictionary → O(N) where N is the length of order
    Iterating through text → O(M) where M is the length of text
    Overall Complexity: O(N + M)
    Space Complexity: O(n) - storing the order
    """
    order_dict = {}
    for i, char in enumerate(order):
        order_dict[char] = i
    #print(order_dict) = {'a': 0, 'b': 1, 'c': 2, 'd': 3}

    max_seen_index = -1
    for char in text:
        if char in order_dict:
            if order_dict[char] < max_seen_index:
                return False
            max_seen_index = order_dict[char]

    return True

# Test cases
print(orderRule("abcd", "axubbxcxbxd"))  # False
print(orderRule("abcd", "abcd"))  # True
print(orderRule("abcd", "aabbccddc"))  # False
print(orderRule("abcd", "abcde"))  # True
print(orderRule("abcd", "aaaabbbbccccdddd"))  # True
