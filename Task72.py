# Function to calculate discounted price
def calculate_discounted_price(original_price, discount_percentage):
    discounted_price = original_price - (original_price * (discount_percentage / 100))
    return discounted_price

# Function to apply discount
def apply_discount(original_price, discount_percentage):
    discounted_price = calculate_discounted_price(original_price, discount_percentage)
    return f"The discounted price is: ${discounted_price}"

# Function to print shopping cart info
def shopping_cart(original_price, discount_percentage):
    print(apply_discount(original_price, discount_percentage))

# Test the function
shopping_cart(50, 20)