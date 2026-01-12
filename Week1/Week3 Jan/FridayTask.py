# Write a function validate_password(password) that:
# Minimum length 8
# Must contain at least one digit
# Must contain at least one uppercase letter
# Return True or False
#
# def validate_password(password):
#     if len(password) < 8:
#         return False
#     digit = False
#     Upper = False
#
#     for char in password:
#         if char.isdigit():
#             digit = True
#         if char.isupper():
#             Upper = True
#     return digit and upper
# password = input("enter your password: ")
#
# if validate_password(password):
#     print("password is valid")
# elif validate_password(password):
#     print("password is valid")
# else:
#     print("password is not valid")
#     print("min len 8")
#     print("Must contain at least one digit")
#     print("Must contain at least one uppercase letter")

'''Write a function validate_password(password) that:
Minimum length 8
Must contain at least one digit
Must contain at least one uppercase letter
Return True or False
'''


'''
Write a function common_elements(list1, list2) that:
Returns a list of common elements (no duplicates)
Input: [1,2,3,4], [3,4,5,6]
Output: [3,4]

'''

'''
Write a function rotate_list(lst, k) that:
Rotates list right by k positions
Example :
    Input: [1,2,3,4,5], k=2
    Output: [4,5,1,2,3]'''

'''
Write a function common_elements(list1, list2) that:
Returns a list of common elements (no duplicates)
Input: [1,2,3,4], [3,4,5,6]
Output: [3,4]

'''
def common_elements(list1, list2):
    result = []

    for i in list1:
        if i in list2 and i not in result:
            result.append(i)
    return result
list1 = input("enter 1st list : ")
list2 = input("enter 2nd list : ")
common = common_elements(list1,list2)
print("common elements:", common)