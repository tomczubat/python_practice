
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  # To handle an empty list and avoid division by zero
 
    total = sum(numbers)
    average = total / len(numbers)
    return average


print([1,2,3, 5,10])