# import sys

# def build_parent_map(relationships):
#     """Creates a dictionary mapping each employee to their direct manager."""
#     parent_map = {}  # Maps each employee to their direct manager
#     for employee, manager in relationships:
#         parent_map[employee] = manager
#     print(f"Parent Map: {parent_map}")
#     return parent_map

# def get_ancestors(parent_map, employee):
#     """Finds all ancestors of a given employee and their distance."""
#     ancestors = {}
#     level = 0
#     while employee in parent_map:
#         manager = parent_map[employee]
#         ancestors[manager] = level + 1
#         employee = manager
#         level += 1
#     print(f"Ancestors of {employee}: {ancestors}")
#     return ancestors

# def find_levels_between(relationships, emp1, emp2):
#     """Finds the number of levels between two employees."""
#     # Build the parent map
#     parent_map = build_parent_map(relationships)
    
#     # Find all ancestors for both employees
#     ancestors1 = get_ancestors(parent_map, emp1)
#     ancestors2 = get_ancestors(parent_map, emp2)
    
#     # Find common managers
#     common_managers = set(ancestors1.keys()) & set(ancestors2.keys())
#     print(f"Common Managers between {emp1} and {emp2}: {common_managers}")
    
#     if not common_managers:
#         return -1  # No common manager found
    
#     # Find the closest common manager by total distance
#     min_distance = min(ancestors1[manager] + ancestors2[manager] for manager in common_managers)
#     return min_distance

# # Test input
# input_data = [
#     "Susan/Amy",
#     "Susan/John",
#     "John/Amy"
# ]

# # Parsing input
# emp1, emp2 = input_data[0].strip().split('/')
# relationships = [line.strip().split('/') for line in input_data[1:]]

# # Call the function
# result = find_levels_between(relationships, emp1, emp2)

# # Print the result
# print(f"Result: {result}")  # Should print: 2







# a happy number is defined by the following process
# starting with any positive integer, replace a number by the sum of the squares of its digits and repeat the process until the number equals one (where it will stay), or it loops endlessly in a cycle which does not include one, those numbers for which this process ends in one are happy numbers, while those that do not end in one are unhappy numbers.

# input
# your program should read lines of text from standard input. Each line contains a single positive integer
# output.
# If the number is a happy number, print one to standard output otherwise print zero. 
# for example, here is why 7 is a happy number, so 7->49->97->130->ten->one, and he is why 22 is not a happy number. 22, eight, 64, 52, 29,85, 89, 145, 42, 20, 4, 16, 37, 58, 89, and so on 

# so for the tests, for example, the test input is one expected output is one. uh, the test input is seven expected output is one. If the test input is 22 expected output is zero
# 16+81 +49

def happy_number(n):
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)

        n = sum(int(digit) ** 2 for digit in str(n))

    return 1 if n == 1 else 0

print(happy_number(7)) #1
print(happy_number(22)) #0
print(happy_number(1)) #1


