def is_anagram(a: str, b:str):
    # list_a = list(a)
    # list_b = list(b)
    # list_a.sort()
    # list_b.sort()
    # return list_a == list_b

    # OR
    # return sorted(a) == sorted(b)

    # OR
    return count_letters(a) == count_letters(b)

def count_letters(string):
    sc = {}
    for l in string:
        sc[l] = string.count(l)
        print(sc)
    return sc
    # OR 
    # return {l: string.count(l) for l in string}


print(is_anagram('hello', 'olleh'))
