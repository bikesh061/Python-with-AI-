#task
'''
if ==
elif >
elif <
elif <=
elif >=
elif !=                    any str, bolea,int
else
'''

marks = int(input("Enter your marks: "))

if marks == 100:
    print("Perfect score")
elif marks > 80:
    print("Distinction")
elif marks >= 60:
    print("First division")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
