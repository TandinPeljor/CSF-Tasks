user_name = input("Enter a name: ")
i = 0  
vowels = "aeiou"  
vowel_count = 0 

while i < len(user_name):
    if user_name[i] in vowels:
        vowel_count += 1 
    i += 1  

print(vowel_count) 