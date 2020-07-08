print("Program for random color till user wants said it stop")

import random

colors = ["white","black","red","green","blue","yellow","purple","grey",]

while True:
    color = colors[random.randint(0,len(colors)-1)]
    guess = input("I am thinking about a color, can you guess it ? Please write: ").lower()

    while True:
        if(color == guess):
            break
        else:
            guess = input("Nope. Try again:").lower()
    
    print("I was thinking about", color)

    play_again = input("Lets Play again? Press enter to play again OR type 'NO' to quit.").lower()

    if play_again == "no":
        break

print("It was fun thanks for Playing.")

