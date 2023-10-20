# Function to calculate area
def calculate_area(length, width):
    return length * width

# Function to calculate perimeter
def calculate_perimeter(length, width):
    return 2 * (length + width)

# Function to print rectangle info
def rectangle_info(length, width):
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    print("Area: ", area)
    print("Perimeter: ", perimeter)

# Test the function
rectangle_info(4, 5)