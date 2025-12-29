#upper case and Lower case
firstName = "bikesh"
(firstName.upper())    #creates "Bikesh" tempo
print(firstName)       #still prints "bikesh"

firstName = firstName.upper()    #permanent uppercase in the variable
print(firstName.upper())      #now prints BIKESH

lastName = "SHAKYA"
print(lastName.lower())

print(f'{firstName} {lastName.lower()}')
print(f'{firstName.lower()} {lastName.lower()}')   #() runs the function to get result

print("bikesh shakya" .title())     #.title() capitalize the first letter of every word

print("bikesh" .index("s")) #index = “where the letter is?” starting from 0

