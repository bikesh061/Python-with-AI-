# for in loop
my_dictionary = {
                 'first name' : 'bikesh',
                 'Last name' : 'shakya'
}

# for var in my_dictionary:
#     print(var)                     # var = 'first name'  var = 'last name'  key print vayera aaunxa
#
# for var in my_dictionary:
#     print(my_dictionary[var])

for var in my_dictionary.values():
    print(var)

# for var in my_dictionary.values():
#     print(var)

# .keys()
# var = 'first name'
# var = 'last name'

# .values()
# var = 'bikesh'
# var = 'shakya'

 #forkey and value
for var in my_dictionary.items():
    print(var)

# If u need just a key or value
for key,value in my_dictionary.items():
    print(key)