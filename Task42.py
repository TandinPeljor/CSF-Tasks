user_name = input("Enter a name: ")
i = 0 
vowels = "aeiou"

while i < len(user_name):
    if user_name[i] in vowels:
        print(True)
        break
    i += 1
else:
    print(False)