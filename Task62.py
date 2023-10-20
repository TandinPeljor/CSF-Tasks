user_inputs = []
for i in range(3):
    user_input = int(input("Please enter a number: "))
    user_inputs.append(user_input)

def is_even(numbers):
    for number in numbers:
        if number % 2 != 0:
            return False
    return True
    
print(is_even(user_inputs))