#operator modules /operator Remainder dinxa  %

print(15 % 2)

#Task odd, even checker
#1. Take a number from a user
#2. check if the number is even or odd
num = int(input("enter a number: "))
if num%2 ==0:               % gives a remainder, 0 means even
    print(f'{num} is even'  )  #f-string prints the number in the message
else:
    print(f'{num}  is odd')

