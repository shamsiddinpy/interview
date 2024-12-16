from collections import Counter

sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
word = "ab"
start = 0
count = 0
while start <= len(sequence) - len(word):
    if sequence[start:start + len(word)] == word:
        count += 1
    start += 1
print(count)
