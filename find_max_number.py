numbera =  [5, 9, 2, 12, 7]

def find_max_number(numbers):
    if numbers:
        return max(numbers)
    else:
        return None
        
print(find_max_number(numbera))