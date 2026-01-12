# '''write a pyhton function merge_dicts that Takes two dictionaries as input and
# return a new dictionary that merge the two. if there are overlapping keys, the values in the second dectionaryes
# should overwrite the values in thr fisrt dixtionary
# '''

def merge_dicts(dict1, dict2):
    merged_dict = {}                   # if we need to add we must create a new container for dictionary
    for key, item in dict1.items():
        merged_dict[key]= item
    for key, item in  dict2.items():
        merged_dict[key]= item
    return merged_dict
dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'b':4,'d':5}

result = merge_dicts(dict1, dict2)
print(result)


# P Y T H O N
# 0 1 2 3 4 5
# P   Y   T   H   O   N
#-6  -5  -4  -3  -2  -1

#noun --> is palindrome
#noun --> not a palindrome

def is_palindrome(word):
    reversed = ''
    for i in range(1,len(word)+1):
        reversed = reversed + word[-i]
    if reversed == word:
        return True
    else:
        return False

print(is_palindrome('word'))

'''
#Write a python function count_vowels that takes a string as input and returns a dictionary containing
# the count of each vowel (a,e,i,o,u) present in the string

The function should:

Be case-insensitive

only include vowels that appears at least once

text = "programming is Awesome"
print(count_vowels(text))

{'a':2, 'i':1 'o' : 2, 'e' : 2}
'''
vowels = ['a', 'e', 'i', 'o', 'u']
def count_vowels(word):
    vowel_count = {}
    for char in word:
        if char.lower() in vowels:
            if vowel_count[char.lowe]
            # vowel_count[char.lower()] +=1
    return vowel_count
print(count_vowels("programming is Awesome"))
