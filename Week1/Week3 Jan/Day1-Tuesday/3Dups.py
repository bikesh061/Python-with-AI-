# Write a python function called remove_duplicates that take a list of num as parameter
# and returns a new list with all duplicate values removed, while keeping the original order.
# example Input[1.2.2.3.4.3.5]  Output [1,2,3,4,5]

def dups(arr):
    non_dups = []
    for i in arr:
        if i not in non_dups:
            non_dups.append(i)
    return non_dups

print(dups([1,2,2,3,4,3,5]))









