user_name = input("Enter a name: ") 
vowels = "aeiou"
vowel_count = 0 

for i in user_name:  
    if i in vowels:
        vowel_count += 1  

print(vowel_count) 