def find_unique_elements(lst):
    
    return len(set(lst))


lst = [1,2,2,2,3,3,3,3,3,3,4]
print(find_unique_elements(lst))

#The function, find_unique_elements, takes a list (lst) as input and returns the number of unique
#  elements in that list. Here's how it works:
# set(lst): This converts the list lst into a set. A set is a collection of unique elements,
#  so any duplicate elements in the list will be removed, leaving only the unique elements.
#len(set(lst)): This calculates the length of the set obtained in the previous step. Since
#  each element in the set is unique, the length of the set will give you the count of unique 
# elements in the original list.
#So, essentially, the function returns the count of unique elements in the input list.
