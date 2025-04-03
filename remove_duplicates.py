
def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


print(remove_duplicates([1,1,2,2,2,3,5,56,55,56]))

