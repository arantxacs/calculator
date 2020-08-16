list_food = ["pizza", "hamburguesa", "spaguetti", "ceviche", "quesadillas"]

count = 0 

x = len(list_food)/2
if x % 1 == 0.5:
    x= x + 0.5

for food in list_food:
    print("my favorite food is " + food)
    count = count + 1
    if count == x:
        break

