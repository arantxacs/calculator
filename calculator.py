import sys

# step 1 Say Hi and ask for operation.
print("Hi user, this is your calculator")
print("What operation you wanna do?")
#Comand
print("- For the sum (+)")
print("- For the substraction (-)")
print("- For the multiplication (*)")
print("- For the Division (/)")

# step 2 read and whait for the answer
answer = input()
print(f'Your answer is {answer}')

#step 3 parse and decide answer
if "+" == answer:
    print("you want to do a sum")
elif "-" == answer:   
    print("you want to do a substraction") 
elif "*" == answer:   
    print("you want to do a multiplication") 
elif "/" == answer:   
    print("you want to do a division") 
else: 
    print("I don't know what you want")
    