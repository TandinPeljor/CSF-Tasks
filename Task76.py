def is_sorted(numbers):
    # Iterate over the list of numbers
    for i in range(len(numbers) - 1):
        # If the current number is greater than the next one,
        # the list is not sorted in ascending order
        if numbers[i] > numbers[i+1]:
            return False
    # If we haven't returned False during the iteration,
    # it means the list is sorted in ascending order
    return True

print(is_sorted([1, 2, 3, 4, 5])) 
print(is_sorted([5, 4, 3, 2, 1]))  