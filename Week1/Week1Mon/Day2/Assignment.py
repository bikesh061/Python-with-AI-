#Assignment
# find the length and maximum index of string "Hello Python" with the help of len() and manaul medium

name = "Hello Python"
length = 12
index = length - 1
print(name[index])         #prints 'n' the last character
print(f"the length of the name is {length} and maximum index is {index}")
print(len(name))
print(len(name)-1)

#Find index of "p"

print(name[6])

#Replace O with a
print(name.replace("o" , "a"))

#Make all the letter to uppperCase
print(name.upper())

#Acess the letter "y" with the help of index (hint : use - [])
print(name[-5])

#Split the word with '<space>'
print(name.split(" , "))