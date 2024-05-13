def add(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def mul(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

while True:
    print("################")
    print("Calculator")
    print("1: Add")
    print("2: Sub")
    print("3: Mul")
    print("4: Div")
    print("5: Quit")

    option = input("Select your option:1,2,3,4,5:")

    if option == '5':
        print("exiting program:")
        break
    if option in('1', '2', '3', '4'):
        num1 = float(input("enter your first number"))
        num2 = float(input("enter your second number"))

        if option == '1':
            print("Result is ",add(num1, num2))
        elif option =='2':
            print("Result is :", sub(num1, num2))
        elif option =='3':
            print("Result is:", mul(num1, num2))
        elif option =='4':
            print("Result is :", div(num1, num2))
    else :
        print("invalid option selected.....")


