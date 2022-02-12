#Chapter 6 Creating Word count

"""Tokenizing a string and counting unique words."""

#Into to Winston Churchill's Sinews of Peace Speech

text = ('I am glad to come to Westminster College this afternoon and am complimented '
        'that you should give me a degree The name Westminster is somehow familiar to me '
        'I seem to have heard of it before Indeed it was at Westminster that I received ' 
        'a very large part of my education in politics dialectic rhetoric and one or two other things ' 
        'In fact we have both been educated at the same or similar or at any rate kindred establishments')

word_counts = {}

# count occurrences of each unique word
for word in text.split():
    if word in word_counts: 
        word_counts[word] += 1  # update existing key-value pair
    else:
        word_counts[word] = 1  # insert new key-value pair

print(f'{"WORD":<18}COUNT')

for word, count in sorted(word_counts.items()):
    print(f'{word:<18}{count}')

print('\nNumber of unique words:', len(word_counts))
