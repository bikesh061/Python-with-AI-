#Task : input from user for 5 items
'''
item = []
for i in range(5):
    num = int(input(f"enter number {i+1}: "))
    item.append(num)
print("your number are:",item)
'''

#Ask the user to enter 5 numbers and store them in a list. Print the list after all numbers are entered.
#Hint: Use input() inside a loop and append() to add values to the list.

'''
number = []

for i in range(5):
    num = int(input(f"enter number {i+1}: "))
    number.append(num)
print("your number are: ", number) '''

# 2. Loop Question
# Write a Python program that prints numbers from 1 to 10 using a loop.
# Hint: Use a for loop with the range() function.
'''
for i in range(1,11):
    print(i)
   '''

#3. Input Question
# Ask the user to enter a number and check whether the number is even or odd.
# Hint: Use input() to take the number and the % operator to check even or odd.
'''
num = int(input("enter a number: "))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")
   '''

'''
#Write a Python program that:
#Asks the user how many numbers they want to enter.
#Uses a loop to take that many numbers as input.
Stores all the numbers in a list.

Finally:

Prints the list

Prints the sum of the numbers

Prints the largest number in the list
'''

n = int(input("How many number do u want to enter?: "))
number = []
for i in range(n):
     num = int(input(f"enter a number {i+1}: "))
     number.append(num)
print("list",number)
print("sum" ,sum(number))
print("largest number",max(number))