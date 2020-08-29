def suma(first_parameter, second_parameter):
    return first_parameter + second_parameter

def rest(first_parameter, second_parameter):
    return first_parameter - second_parameter

def division(first_parameter, second_parameter):
    return first_parameter / second_parameter

def multiplication(first_parameter, second_parameter):
    return first_parameter * second_parameter

def pow(first_parameter, second_parameter):
    return (first_parameter ** second_parameter)

def modul(first_parameter, second_parameter):
    return (first_parameter % second_parameter)

def mymodul(first_parameter, second_parameter):
    return first_parameter % second_parameter

def main(): 
    print("line")
    print(suma(2, 3))
    print(rest(2, 3))
    print(division(2, 3))
    print(multiplication(2, 3))
    print(pow(2, 3))
    print(modul(2, 3))
    print(mymodul(2, 3))

main()    