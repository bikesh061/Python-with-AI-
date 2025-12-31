#Task input from user for 5 items

items= []
for i in range(5):
    item = input(f"Enter item {i+1}: ")
    items.append(item)
    print(items)

#Ask the user to enter 5 numbers and store them in a list. Print the list after all numbers are entered.
#Hint: Use input() inside a loop and append() to add values to the list.

numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("The numbers you entered are:", numbers)