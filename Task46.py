# factorial:
# the product of all positive integers less than or equal to a given positive integer 
# denoted by that integer and an exclamation point.

user_number = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= user_number:
    factorial *= i
    i += 1

print(factorial)
