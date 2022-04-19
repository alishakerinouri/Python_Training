from itertools import count
import random
correct_number = random.randint(0,1000)
counter = 0

def start():
    print("""
    Welcome to guess the number game :)
    In this game, you should guess a name which the computer generats it from 0 to 1000,randomly!
    Hope you enjoy this game ;)
    """)
    name = input("What's your name?\n")
    print('Oh nice to meet you '+name+ " , Now let's start the game!")



def game():
    while True:
        try:
            guess_number = int(input("please guess a number in range of 0 to 1000 >>> "))
            global counter
            counter +=1
            if guess_number == correct_number:
                print("perfect! "+ str(guess_number) + " is the answer!")
                print("You guess it by "+ str(counter)+ " times")
                break
            elif guess_number < correct_number:
                print("It's Higher!")
                continue
            elif guess_number > correct_number:
                print("It's Lower!")
                continue
        except ValueError:
            print("Please write a number. What you entered is not a number.")
            continue

start()
game()
