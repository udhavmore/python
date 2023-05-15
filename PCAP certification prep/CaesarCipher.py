"""
Based on a given number, shift the position of the alphabets by that number.
e.g. 
number = 3
A, B, C, D will shift by 3 numbers
0, 1, 2, 3 and so the new alphabets will be
D, E, F, G
e.g.
hello -> mjqqt (shift=5)
mjqqt -> hello (shift=5)
"""

alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # Taking 2nd set of alphabet to use shift=30



def encrypt(msg, shift):
    encrypted_msg = ""
    for char in msg:
        idx = alphabet.index(char)
        new_idx = idx + shift
        encrypted_msg += alphabet[new_idx]
    
    print(encrypted_msg)


def decrypt(cypher, shift):
    decrypted_msg = ""
    for char in cypher:
        idx = alphabet.index(char)
        new_idx = idx - shift
        decrypted_msg += alphabet[new_idx]
    print(decrypted_msg)

def ceasar_cypher():
    while True:
        operation = input("Do you want to 'encode' or 'decode': \n")
        if 'exit' in operation:
            exit()
        msg = input('Enter your message: \n').lower()
        shift = int(input('Enter shift number: \n'))

        if 'encode' in operation:
            encrypt(msg, shift)
        elif 'decode' in operation: 
            decrypt(msg, shift)
        


print(ceasar_cypher())