# def greet():
#     print("hello")
# greet()

# write a funcion to give count of vowels in a word
def count_vowel(word):
    vowels = "aeiouAEIOU"
    count = 0

    for char in word:
        if char in vowels:
            count += 1

    return count
word = input("Enter a name: ")
print(count_vowel(word))




