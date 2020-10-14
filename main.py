# This is a sample Python script.
from itertools import chain, permutations

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# define all lists
letters = []
words_created = []
words_accepted = []
dict_under_9 = []
PermutationsNumber = 0


# define the Permutation function
def permutate(iterable_string):
    iterable_list = list(iterable_string)
    return chain.from_iterable(permutations(iterable_list, r) for r in range(len(iterable_list) + 1))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('Collins Scrabble Words (2019).txt', 'r') as f_in:
        dict_under_9 = f_in.read().splitlines()

    in_string = str(input("Insert letters here > "))
    print(in_string)
    print(list(in_string))
    print("Processing...")
    # print("dict_u9:", dict_under_9)
    # words_created = list(permutate(in_string))
    print("words_created =", words_created)
    for elem in permutate(in_string):
        PermutationsNumber += 1
        word = ''.join(elem)
        if word.upper() in dict_under_9 and len(word) > 2:
            if word.upper() not in words_accepted:
                words_accepted.append(word)

    # removing duplicates because of string equality
    words_accepted = list(dict.fromkeys(words_accepted))
    words_accepted.sort()

    for i in range(2, len(in_string)+1):
        print("----------- {0} ----------".format(i))
        temp_list = []
        for wa in words_accepted:
            if len(wa) == i:
                # print("words_accepted:", words_accepted)
                temp_list.append(wa)
                # print(wa)
        print(temp_list)
