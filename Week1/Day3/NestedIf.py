#Nested If
name = "bikesh"
#num = 1
num = 2
num1 = 2             #define num1

if name == "bikesh":          #check first Condition
    print("executes")
    if num == 3:             #check  second condition inside first  ( num ==2 , beacause you set num = 2
        print("nested if exceuted")
        if num1 == 2 :        # check third condition inside second
            print("hello")