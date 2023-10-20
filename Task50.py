num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = 0

while num1 <= num2:
    sum += num1
    num1 += 1

print("The sum of all numbers between is", sum)