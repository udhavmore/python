def capital_indexes(word: str):
    index_list = []
    for i in range(len(word)):
        if word[i] == word[i].capitalize():
            index_list.append(i)
    return index_list


print(capital_indexes("HeLlO"))

from string import ascii_uppercase

def cap(x):
    return [i for i in range(len(x)) if x[i] in ascii_uppercase]

print(cap("HeLlO"))
