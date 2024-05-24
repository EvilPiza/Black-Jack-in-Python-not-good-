#Black Jack

#I made this for a project btw so idrc

import random

plr_amount = 0
maximum_amount = 21 #you can change this ig
bot1 = random.randint(5, 10)
bot2 = random.randint(7, 11)
bot_amount = bot1 + bot2
print("The bot's first card is a " + str(bot1))
def action():
    global plr_amount
    global maximum_amount
    while plr_amount < maximum_amount:
        inp = str(input("Action: "))
        if inp == "hit" or inp == "h":
            hit()
        if inp == "stay" or inp == "s":
            stay()
    if plr_amount > maximum_amount:
        pass
        
def hit():
    r = random.randint(1,11)
    global plr_amount
    global maximum_amount
    global bot1
    if plr_amount < maximum_amount:
        plr_amount += r
        print("You pulled a " + str(r))
        print(" ")
        print("Your total is " + str(plr_amount))
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
        
action()
    
    
    
    
    
    
    
