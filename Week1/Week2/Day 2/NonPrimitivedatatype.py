# non primitive data type
# data types made up of multiple or same kind of primitive data types
# Collection of primitive data types./*-+QAX-=[]\;E3WUJIO8,L./
from operator import index
'''
# list
age = 20
name = "Bks"
weight = 60


#list are encloed in big brackets --> []
#List allows multiple data types
#List is indexed data type
info = [20,"bks",60,True]
print (info)
#index : 0  1  2  3

#index wise access
print(info[2])
'''

#primitive Data Types
'''
int
float
bool
str
'''
info = [20,"bks",60,True]
#print (info)
#index : 0  1  2  3

#index wise access
#print(info)
# for in loop in list

#for i in info:
 #  print(i)

 #Task While loop to iterate over the info list
 #hint : use access by index
#i = 0
'''
while i < len(info):
    print(f'index of {info[i]} is {i}')
    i+=1 '''

#list operation

# .append()
#info = [20,"bks",60,True]
#info.append(6)
#print(info)

# .clear()
#info.clear()
#print(info)

# .index()
#print(info.index(60))

# .pop()
#info = [20,"bks",60,True]  pop le last ko element Remove garxa
#print(info.pop())
#print(info)00

# replacing values in list
# info = [20,"bks",60,True] --> info[1] = 30 --> [20,30,"bks",60,True]
#info[1]=30
#print(info)

# .insert()
# info = [20,"bks",60,True] --> info.insert(index_value, element) --> [20,"pkr""bks",60,True]

#info.insert(1, "PKR")
#print(info)

# Task
# Take a input from user for 5 items' price

#Store thoes prices in a list

# runa for in loop to calculate the total price

#print the final total amount with 13% VAT

#Hint for Vat:
print(100- 0.16)