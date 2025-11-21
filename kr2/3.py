words = input("ввести слова, розділені пробілами ").strip().split()
def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
print(f"The longest word is: {longest_word(words)}")