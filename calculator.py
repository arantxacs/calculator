import sys

# Step 1 Say Hi and ask for operation.
print("Hi user, this is your calculator")
print("What operation you wanna do?")
#Comand
print("- For the sum (+)")
print("- For the substraction (-)")
print("- For the multiplication (*)")
print("- For the Division (/)")

# Step 2 read and whait for the answer
answer = input()


# Step 3 parse and decide answer,ask for the parameters
if (answer == "+") or (answer == "-") or (answer == "/") or ( answer == "*"):
    print("Give the first parameter")
    x= input()
    print("Give the second parameter")
    y = input()


if "+" == answer:
    print("you want to do a sum")
    result = int(x) + int(y) 
    
elif "-" == answer:   
    print("you want to do a substraction")
    result = int(x) - int(y) 
    
elif "*" == answer:   
    print("you want to do a multiplication") 
    result = int(x) * int(y) 
   
elif "/" == answer:   
    print("you want to do a division") 
    result = int(x) / int(y) 
else: 
    result = ""
    print("I don't know what you want")

if result != "":
    print(f'your answer is {result}')

    

