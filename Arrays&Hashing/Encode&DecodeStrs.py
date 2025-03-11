# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is 
# decoded back to the original list of strings.

# Machine 1 (sender) has the function:

# string encode(vector<string> strs) {
#   // ... your code
#   return encoded_string;
# }
# Machine 2 (receiver) has the function:
# vector<string> decode(string s) {
#   //... your code
#   return strs;
# }
# So Machine 1 does:

# string encoded_string = encode(strs);
# and Machine 2 does:

# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.

# Implement the encode and decode methods.

# You are not allowed to solve the problem using any serialize methods (such as eval).

 

# Example 1:

# Input: dummy_input = ["Hello","World"]
# Output: ["Hello","World"]
# Explanation:
# Machine 1:
# Codec encoder = new Codec();
# String msg = encoder.encode(strs);
# Machine 1 ---msg---> Machine 2

# Machine 2:
# Codec decoder = new Codec();
# String[] strs = decoder.decode(msg);
# Example 2:

# Input: dummy_input = [""]
# Output: [""]


class Codec:
    def encode(self, strs:List[strs])-> str:
        """
        Encodes a list of strs to a single str
        """

    #our input is a list of str, and we want to encode to a str then decode to a list of strs
    #we want to know where a word starts and where it ends
    #we can store the len of the word at the beginning to show how far the word goes then use a delimiter to indicate strat of a word
    #
                #dummy_input = ["Hello","World"] --> "HelloWorld" --> ["Hello","World"]
                #so we encode with the backspace char  "5#Hello5#World"

        ans = ""
        for word in strs:
            length = len(word) #5
            ans += str(length) + "#" + word # --> "5#Hello5#World"
        return ans

    
    def decode(self, s:str) ->List[str]:
        """
        decodes a single str to a list of strs
        """
        #   s = "5#Hello5#World"  --> ["Hello","World"]
        res = [] #where we append our decoded str
        ptr = 0 #loop thru

        while ptr < len(s): #we are in bounds
            num = ""
            while s[ptr] != "#":
                num += s[ptr] #  "5"
                ptr += 1
            num = int(num) # "5" --> 5

            ptr += 1 #skip the backspace

            word = s[ptr: ptr+num] #slice the word and append to res
            res.append(word)

            ptr += num 
        return res





