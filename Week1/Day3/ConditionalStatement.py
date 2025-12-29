#conditional Statement
from turtledemo.round_dance import stop

condition = True
if condition :                 #is condition true?
    print("Yes")             # true = yes = allow      false = No = stop

condition = int(input("enter a number: "))
if condition == 1:
    print("if executed")
elif condition == 2:                     #if/elif/else = check condition
    print("elif executed")
else:
    print("else executed")


''' age = 22
if age >= 25:
    print("you can vote")
  '''

'''light = input("enter trafic light color: ")
if light == "red":
    print("stop")
elif light == "yellow":
    print("Wait")
else:
    print("Go")
'''