"""
Word Occurrences
Estimate: 5 minutes
Actual:   6 minutes
"""

text = input("Text: ")
words = text.split()
word_to_count = {}
maximum_word_length = max(len(word) for word in words)

for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

for word, count in sorted(word_to_count.items()):
    print(f"{word:{maximum_word_length}} : {count}")
