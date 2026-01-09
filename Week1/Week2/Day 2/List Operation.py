# List Operation
from linecache import clearcache

info = [20,"bikesh",60.23,"bikesh",True]

# .append()
#info.append("Shakya")           # add at end
#print(info)

# .clear
#info.clear()
#print(info)

# .index()
#print(info.index("bikesh"))

#.pop()n        list ko last element lai hataunxa
#
print(info.pop())
print(info)

# Replacing values in list
#[20,"bikesh",60.23,"bikesh",True]

info[2] = 69
print(info)