def find_longest_word(input_string):
    # Split the string into words
    words = input_string.split()
    
    # Find the longest word
    longest_word = max(words, key=len)
    
    # Return the longest word
    return longest_word

print(find_longest_word("Trust yourself that you can do it and get it"))