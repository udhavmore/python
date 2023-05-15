# import random
#
# marvel = ['Ironman', 'Thor', 'Captain America', 'Black Widow']
# print(marvel)
# marvel.append('Hulk')
# print(marvel)
# new_heroes = ['Captain Marvel', 'Scarlet Witch', 'Doctor Strange']
#
# marvel.extend(new_heroes)
# print(marvel)
#
# string = 'Ironman, Thor, Captain America, Black Widow, Hulk, Captain Marvel, Scarlet Witch, Doctor Strange'
#
# hero = string.split(',')
# super_hero = random.choice(hero)
# print(f"{super_hero.strip()} saved the day")
#
#
# avengers = [marvel, new_heroes]
# print(avengers)


# print("""
#      1    2    3
# 1 ['⬜', '⬜', '⬜']
# 2 ['⬜', '⬜', '⬜']
# 3 ['⬜', '⬜', '⬜']
# """)
# row1 = ['⬜', '⬜', '⬜']
# row2 = ['⬜', '⬜', '⬜']
# row3 = ['⬜', '⬜', '⬜']
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# mark_pos = input("Position for X mark: ")
#
# hor, ver = int(mark_pos[0]), int(mark_pos[1])
# map[ver-1][hor-1] = 'X'
# print(f"{row1}\n{row2}\n{row3}")

# Average
# height_list = [155, 132, 110, 160, 158]
# sum_height, total = 0, 0
# for i in height_list:
#     sum_height += i
#     total += 1
# # alternate
# sum_height = sum(height_list)
# print(sum_height)
# avg_height = sum_height / total
# print(f"Average Height: {avg_height}")

# # Highest Value
# nos = [3, 66, 98, 20, 11, 32, 102]
# print(nos)
# highest_num = 0
# for i in nos:
#     if i > highest_num:
#         highest_num = i
# print(f"Highest Number: {highest_num}")
# # alternate
# print(max(nos))

# # Add all Even numbers
# total = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         total += 1
# print(total)
# # Alternate
# total = 0
# for i in range(2, 101, 2):
#     total += 1
# print(total)

# # FizzBuzz
# # print numbers but if a number is divisible by 3 print fizz and if number is divisible by 5, print buzz &
# # if divisible by both 3 and 5 print FizzBuzz
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# # PyPassword Generator
# import random
# import string
#
# alpha_lower = list(string.ascii_lowercase)
# alpha_upper = list(string.ascii_uppercase)
# alpha_upper.extend(alpha_lower)
# alphabets = alpha_upper
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
#
# pass_len = int(input("Length of Characters: "))
# num_len = int(input("Number of Digits: "))
# sym_len = int(input("Number of Symbols: "))
# password = []
#
# for i in range(pass_len):
#     pass_alpha = random.choice(alphabets)
#     password.append(pass_alpha)
#
# for i in range(num_len):
#     pass_num = random.choice(numbers)
#     random_num_position = random.randint(0, pass_len)
#     password.insert(random_num_position, pass_num)
#
# for i in range(sym_len):
#     pass_sym = random.choice(symbols)
#     random_sym_position = random.randint(0, pass_len)
#     password.insert(random_sym_position, pass_sym)
#
# random.shuffle(password)
# password_str = ""
# for char in password:
#     password_str += str(char)
#
# print(f"Shuffled Password: {password_str}")


