# A pangram is a phrase or sentence containing every letter (a-z) in the English alphabet.
#  Given a string, determine if it is a pangram. / Given a string, return True  if it contains
#  all English alphabet letters and False if not


def is_pangram(sentence):
    """
    Time Complexity: O(n) - iterate through the string
    Space Complexity: O(n) - storing unique letters
    """
    # Convert to lowercase for case insensitivity
    sentence = sentence.lower()
    # Create a set to store unique letters
    letter_set = set()
    # Iterate through the string
    for char in sentence:
            if char.isalpha() and char.islower():
                letter_set.add(char)
    # A pangram must have all 26 letters
    return len(letter_set) == 26

# Example Test Cases
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
print(is_pangram("Hello world"))  # False
print(is_pangram("abcdefghijklmnopqrstuvwxyz"))  # True
print(is_pangram("The five boxing wizards jump quickly"))  # True
print(is_pangram("Missing letters"))  # False
