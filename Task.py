def Addition(num1, num2):
    return num1 + num2
def Subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    return num1 / num2

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operation = input("Input a operations(+,-,*,/):")

if operation == '+':
    print (num1 + num2)
elif operation == '-':
    print (num1 - num2)
elif operation == '*':
    print (num1 * num2)
elif operation == '/':
    print (num1 / num2)
