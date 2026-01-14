'''
Write a Python function called count_word_frequency(sentence) that:
Takes a string sentence as input. Ignores case sensitivity (treat "Python" and "python"
as the same word). Removes punctuation (.,!?). Returns a dictionary where: Keys are unique words in the sentence
Values are the number of times each word appears
sentence = "Python is great, and Python is fun!"
print(count_word_frequency(sentence))
result : {'python': 2, 'is': 2, 'great': 1, 'and': 1, 'fun': 1}
'''

def count_word_frequency(sentence):
    sentence = sentence.lower()

for char in ".,!?:":
    sentence = sentence.replace(char, "")

words = sentence.split()