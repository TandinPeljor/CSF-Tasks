# Function to calculate hypotenuse
def calculate_hypotenuse(side1, side2):
    import math
    hypotenuse = math.sqrt(side1**2 + side2**2)
    return hypotenuse

# Function to print triangle info
def triangle_info(side1, side2):
    hypotenuse = calculate_hypotenuse(side1, side2)
    print(f"The length of the hypotenuse is: {hypotenuse}")

# Test the function
triangle_info(4, 5)