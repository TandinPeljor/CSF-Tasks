user_name = input("Enter a name: ")
vowels = "aeiou" 

for i in user_name: 
    if i in vowels:  
        print(True)  
        break  
else: 
    print(False) 