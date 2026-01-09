# BUild CLI calcuator
'''
1. Take a first number input from user (int)
2. take a second number input from user (int)
3. Take operation input from user : +, -, *, /
4. use if-else ladder to perform thoes operation
5. if the user's operator input is invlaid display aapopriae messae
6. nOte : the output printed should be in float datatype

'''

num = int(input("enter first number: "))
num1 = int(input("enter second number: "))
op = input("enter operation (+,-, *, /): ")
if op == "+":
    print(float(num + num1))
elif op == "-":
    print(float(num - num1))
elif op == "*":
    print(float(num * num1))
elif op == "/":
    print(float(num / num1))
else:
    print("invalid operation")















