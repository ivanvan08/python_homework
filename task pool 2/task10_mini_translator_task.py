
"""
🌍 TASK 10 — Mini Translator
Topic: dictionary lookup with default

Dictionary: {"cat":"кіт", "dog":"собака", "bird":"пташка"}
Source words: ["cat", "dog", "car", "bird"]
Build a result list of translations (or "N/A" if no translation). Print the resulting list.

"""
# TODO: fill result with translations using .get; then print(result)
dictionary = {"cat":"кіт", "dog":"собака", "bird":"пташка"}
source_words = ["cat", "dog", "car", "bird"]
for source in source_words:
    print(dictionary.get(source))