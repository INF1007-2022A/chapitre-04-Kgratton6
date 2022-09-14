

string = 'allo allo cava'
words_list = string.split()
word = 'allo'
total = 0

for i in words_list:
    if i == word:
        total += 1

print(total)
