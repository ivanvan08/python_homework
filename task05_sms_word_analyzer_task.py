"""
Task 5 — SMS Word Analyzer 📱

Requirements:
  - text = "Meeting at 10am in Room 301. Don’t be late!"
  - Split into words
  - For each word, strip leading/trailing punctuation and print "<word> -> <len>"
  - Build a list of tuples like [("Meeting", 7), ...] (optional)

Practice: string splitting, strip punctuation, loops

OUTPUT EXAMPLE
--------------
Meeting -> 7
at -> 2
10am -> 4
in -> 2
Room -> 4
301 -> 3
Don’t -> 5
be -> 2
late -> 4

Tuples: [('Meeting', 7), ('at', 2), ('10am', 4), ('in', 2), ('Room', 4), ('301', 3), ('Don’t', 5), ('be', 2), ('late', 4)]
"""

import string
from string import punctuation #знайшов поки створював змінну

text = "Meeting at 10am in Room 301. Don’t be late!"
print("(Starter) Text:", text)
# TODO: split, clean punctuation with strip, print "<word> -> <len>"
words = text.split()
tuples = []
for i in range(len(words)):
     for word in words:
        print(f"{word.strip(punctuation)} -> {len(word)}")
        tuples.append(f"({f"{word.strip(punctuation)}, {len(word)}"})")
# Optional: build a list of tuples (word, length) and print it
print(tuples)