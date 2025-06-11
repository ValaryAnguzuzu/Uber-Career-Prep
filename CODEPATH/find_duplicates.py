"""
Find All Duplicate Treasure Chests in an Array
Captain Blackbeard has an integer array chests of length n where all the integers in chests are in the range [1, n] 
and each integer appears once or twice. Return an array of all the integers that appear twice, representing the 
treasure chests that have duplicates.
"""
#add the intergers in a dictionary with their counts
#then return count == 2

#use a set st if you see the num for a second time add it to a 

# def find_duplicate_chests(chests):
#     freq = dict()
#     for num in chests:
#         freq[num] = freq.get(num, 0) + 1

#     result = []
#     for key, value in freq.items(): #.items?
#         if value == 2:
#             result.append(key)
#     return result

def find_duplicate_chests(chests):
    freq = set()
    result = []
    for num in chests:
        if num in freq:
            result.append(num)
        else:
            freq.add(num)
    
    return result


chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1)) #[3,2]
print(find_duplicate_chests(chests2))#[1]
print(find_duplicate_chests(chests3))#[]


        
