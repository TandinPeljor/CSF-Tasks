def reverse_words(input_string):
    # Split the string into words
    words = input_string.split()
    
    # Reverse each word and store it in the list
    reversed_words = [word[::-1] for word in words]
    
    # Join the reversed words back into a string
    output_string = ' '.join(reversed_words)
    
    # Return the final string
    return output_string

print(reverse_words("Hello, world!")) 