"""
Rock Paper Scissor
"""
import random
from termcolor import colored


def main():
    print(colored('Welcome to Rock, Paper, Scissor!!!', 'cyan'))
    rock, paper, scissor = 'rock', 'paper', 'scissor'
    options = ['rock', 'paper', 'scissor']
    score_user, score_comp = 0, 0
    while True:
        user = input("Enter your Option "+str(options)+" : ").lower()
        comp = random.choice(options)
        print(f"User: {user}\nComputer: {comp}")

        # user rock
        if user == rock and comp == scissor:
            print(f"User Wins")
            score_user += 1
            score_comp -= 1
        elif user == rock and comp == paper:
            print(f"User Loss")
            score_comp += 1
            score_user -= 1
        elif user == rock and comp == rock:
            print("Draw Match!!!")

        # user paper
        elif user == paper and comp == rock:
            print(f"User Wins")
            score_user += 1
            score_comp -= 1
        elif user == paper and comp == scissor:
            print(f"User Loss")
            score_comp += 1
            score_user -= 1
        elif user == paper and comp == paper:
            print("Draw Match!!!")

        # user scissor
        elif user == scissor and comp == paper:
            print(f"User Wins")
            score_user += 1
            score_comp -= 1
        elif user == scissor and comp == rock:
            print(f"User Loss")
            score_comp += 1
            score_user -= 1
        elif user == scissor and comp == scissor:
            print("Draw Match!!!")

        elif user == 'exit':
            if score_user < score_comp:
                print(colored(f"User: {score_user}", 'red'))
                print(colored(f"Computer: {score_comp}", 'green'))
                print(colored("Computer Wins!!!", 'magenta'))
            else:
                print(colored(f"User: {score_user}", 'green'))
                print(colored(f"Computer: {score_comp}", 'red'))
                print(colored("User Wins!!!", 'magenta'))
            break


if __name__ == "__main__":
    main()
