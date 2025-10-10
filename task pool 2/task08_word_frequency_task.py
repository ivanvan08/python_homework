
"""
📚 TASK 8 — Word Frequency
Topic: strings → list → dictionary (frequency)

Text: "hello world hello python world hello"
Count how many times each word occurs. Print the dictionary sorted by word (key).
"""

# Starter:
text = "hello world hello python world hello"
# TODO: split into words; count frequencies into dict; print in key-sorted order
dict_of_words = {}
list_of_words = text.split(" ")
for word in list_of_words:
    if word in dict_of_words:
        dict_of_words.update({word: dict_of_words[word]+1})
    else:
        dict_of_words.update({word: 1})
print(dict_of_words)
