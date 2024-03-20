import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
           'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',  
           'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P',  
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
           '*', '(', ')', '<'] 
print("Generate your Password")
pass_letters = int(input("please enter how many letters you want in ur password:-"))
pass_numbers = int(input("please enter how many numbers you want in ur password:-"))
pass_symbols = int(input("please enter how many symbols you want in ur password:-"))
password = []
for i in range(pass_letters):
    sel = random.choice(letters)
    password += sel
for i in range( pass_numbers):
    sel = random.choice(numbers)
    password += sel
for i in range( pass_symbols):
    sel = random.choice(symbols)
    password += sel

random.shuffle(password)
passwordc= ""
for i in password:
    passwordc += i
print(passwordc)



   
    
    

