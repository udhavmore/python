import random

word_list = ['hello', 'balloon', 'strawberry', 'hippo', 'tea']
word = random.choice(word_list)
print(word)
counter = 0

empty_word = ''
for i in range(len(word)):
    empty_word = empty_word + '_' + " "

print(empty_word)

for i in range(len(word)):
    user_guess = input("Guess a Character: ").lower()
    print(f'User chose: {user_guess}')
    if user_guess == "":
        print("Enter a character")
    if user_guess in word:
        print("Match found")
    else:
        counter += 1
        print(f"hang {counter}")
        if counter == len(word):
            print("You Dead Bro!!")


words = ["black", "white", "blue"]
result_list = []
word = random.choice(words)
print(word)
user_char = input("Guess the word:")
for i in range(len(word)):
    if user_char == word[i]:
        print(f"Found: {user_char}")
        result_list.append(True)
    else:
        result_list.append(False)

print(result_list)
