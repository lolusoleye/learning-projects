text = "bitcoin is going up bitcoin is pumping bitcoin"

words = text.split()

tally = {}

for word in words:
    if word in tally:
        tally[word] = tally[word] + 1
    else:
        tally[word] = 1

print(tally)