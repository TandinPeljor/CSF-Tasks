def multiply_lists(list1, list2):
    return [a * b for a, b in zip(list1, list2)]
print(multiply_lists([1, 2, 3], [4, 5, 6]))