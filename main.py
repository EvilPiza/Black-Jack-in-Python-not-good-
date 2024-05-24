#Black Jack


print("Welcome to a trashy version of Black Jack!")
print(" ")
print("Make sure you read the README on GitHub for the Controls!")
print(" ")
print(" ")

import random

plr_amount = 0 #this is the starting amount
maximum_amount = 21 #you can change this ig
bot1 = 69 #bot1, bot2, and bot_amount are all integer placeholders btw
bot2 = 420
bot_amount = 34 

def bot_luck():
    global bot1
    global bot2
    global bot_amount
    inp = str(input("Mode: "))
    if inp == "normal" or inp == "n":
        print("Normal Bot Luck Selected!")
        bot1 = random.randint(5,10)
        bot2 = random.randint(6,11)
        bot_amount = bot1 + bot2
        print("The bot's first card is a " + str(bot1))
        action()
    if inp == "lucky" or inp == "l":
        print("Lucky Bot Luck Selected!")
        bot1 = random.randint(7,10)
        bot2 = random.randint(7,11)
        bot_amount = bot1 + bot2
        print("The bot's first card is a " + str(bot1))
        action()
    if inp == "insane" or inp == "i":
        print("Insane Bot Luck Selected!")
        bot1 = random.randint(9,10)
        bot2 = random.randint(8,11)
        bot_amount = bot1 + bot2
        print("The bot's first card is a " + str(bot1))
        action()
    else:
        #DEFAULT LUCK!!!
        print("Default Bot Luck Selected!")
        bot1 = random.randint(5,10)
        bot2 = random.randint(6,11)
        bot_amount = bot1 + bot2
        print("The bot's first card is a " + str(bot1))
        action()

def action():
    global plr_amount
    global maximum_amount
    global bot_amount
    while plr_amount < maximum_amount:
        inp = str(input("Action: "))
        print(" ")
        if inp == "hit" or inp == "h":
            hit()
        if inp == "stay" or inp == "s":
            stay()
    if plr_amount > maximum_amount:
        pass
    if plr_amount == maximum_amount:
        if plr_amount > bot_amount:
            print("You win!")
            print(" ")
            print("Player Amount: " + str(plr_amount))
            print("Bot Amount: " + str(bot_amount))
        if plr_amount == bot_amount:
            print("Draw!")
            print(" ")
            print("Player Amount: " + str(plr_amount))
            print("Bot Amount: " + str(bot_amount))
def hit():
    r = random.randint(1,11)
    global plr_amount
    global maximum_amount
    global bot1
    if plr_amount < maximum_amount:
        plr_amount += r #change r to 21 to always win btw
        print("You pulled a " + str(r))
        print(" ")
        print("Your total is " + str(plr_amount))
        print(" ")
    if plr_amount > maximum_amount:
        print("You lost!")
def stay():
    global bot_amount
    global plr_amount
    if plr_amount > bot_amount:
        print("You Win!")
        print(" ")
        print("Player Amount: " + str(plr_amount))
        print("Bot Amount: " + str(bot_amount))
    if plr_amount < bot_amount:
        print("You lost!")
        print(" ")
        print("Player Amount: " + str(plr_amount))
        print("Bot Amount: " + str(bot_amount))
    if plr_amount == bot_amount:
        print("Draw!")
        print(" ")
        print("Player Amount: " + str(plr_amount))
        print("Bot Amount: " + str(bot_amount))
        
bot_luck()
