i = 0
with open('../english-words/words_alpha.txt', 'r') as f_in, \
     open('words_under_9.txt', 'w') as f_out:
    for line in f_in:
        if len(line) < 9:
            i += 1
            f_out.writelines(line)

print("i =", i)
