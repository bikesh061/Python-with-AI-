# # Write a python function called find_max_min that takes a list of integers as a parameter and returns both the maximum
# and minimum values in the list without using the built-in-max() or min() functions

def find_max_min():































def find_max_min(numbers):
    # Assume the list has at least one element
    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum
nums = [5, 2, 9, 1, 7]
max_val, min_val = find_max_min(nums)
print("Max:", max_val)
print("Min:", min_val)

