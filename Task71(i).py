def find_common_elements(list1, list2):
    return [element for element in list1 if element in list2]
print(find_common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))