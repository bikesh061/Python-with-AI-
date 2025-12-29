#strip and Split

'''
print(name.split())     # default space → ['Bikesh', 'Shakya']
print(name.split(" "))  # same as above → ['Bikesh', 'Shakya']
print(name.split("  ")) # two spaces → no two spaces here, so ['Bikesh Shakya']
print(name.split(","))  # split by comma → ['Bikesh Shakya'] (no comma)
'''

name = "bikesh  "
print(name.strip())  #.strip() → removes spaces at the start and end of a string.

name = "Bikesh Shakya"
print(name.split(" , "))

word = "hello my name is Bikesh"
print(word.strip())

word = word.upper()
print(f'{word}')      #print the value of the variable words
print(word.split())   #splits the string into list of word Example: "HELLO WORLD" → ['HELLO', 'WORLD']
print(name.title())   #make the first letter of each word uppercase