text = input("Paste your text here: ")

words = text.split()

tally = {}

for word in words:
    if word in tally:
        tally[word] = tally[word] + 1
    else:
        tally[word] = 1

print(tally)