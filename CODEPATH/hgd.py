"""
Problem 1: Counting Treasure
Captain Blackbeard has a treasure map with several clues that point to different locations on an island.
 Each clue is associated with a specific location and the number of treasures buried there. 
 Given a dictionary treasure_map where keys are location names and values are integers representing 
 the number of treasures buried at those locations, write a function total_treasures() that returns the 
 total number of treasures buried on the island
"""

#U - Get the sum of the values in the dict
# P - dict.values() -> sum()
#return that

def total_treasures(treasure_map):
    result = treasure_map.values()
    return sum(result)

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

print(total_treasures(treasure_map1)) 
