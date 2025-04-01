def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))
    

print(sum_of_digits(123))
    
#This function, sum_of_digits, takes an integer num as input and returns the sum of its 
# digits. Here's how it works:

#str(num): This converts the integer num into a string. This allows us to iterate over each
#  digit in the number.

#(int(digit) for digit in str(num)): This is a generator expression that iterates over
#  each character (digit) in the string representation of the number and converts each character back to an integer. So, it effectively gives us an iterable of integers representing the digits of the number.

#sum(...): This calculates the sum of all the integers obtained in the previous step. It
#  adds up all the digits of the original number.

#So, the function returns the sum of the digits of the input number.