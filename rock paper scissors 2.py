'''
Author Rami
date 12/1
description of a code block that asks the user if they want to play rock paper scissors. both answers tell them to play anyway and the code continues until the player users say to stop. if someone says scissors they have a 50% chance to get the answer rock 30% chance to get paper and a 20% to get scissors 
bugs Not that I know of 
challenges while loop
sources w3schools Oliver Servedio 
'''

import random#enter the random library
import time#enter the time library 

rps_probabilities = [['rock','rock','rock','rock','rock','paper','paper', 'paper', 'scissors', 'scissors'], ['paper','paper','paper','paper','paper','scissors','scissors','scissors','rock','rock'], ['scissors','scissors','scissors','scissors','scissors','rock','rock','rock','paper', 'paper']]#random list 3
rps_options = ['rock', 'paper', 'scissors']

while True: #the while loop continues until the yes or no question is answered
    play = str.lower(input("do you want to play rock paper scissors?"))#question do you want to play rock paper scissors? and it doesn't matter if its in caps
    #or lowercased
    if play == "yes": #if the answer is yes then it will print yes
        print("lets play!")# if the answer is yes then it will print Let's play
        time.sleep(2)#2-second delay
        break#makes a break so the code doesn't continue
    elif play == "no": #if the answer is no then it will print that's too bad we are gonna play anyways
        print("that's too bad we are gonna play anyways!") #if the answer is no then it will print that's too bad we are gonna play anyways
        time.sleep(2)#2-second delay
        break # a break to make sure the code doesn't continue
    else:#statment if a different answer is given
        print("only yes or no!")# the answer that is given if there is a different answer 
        time.sleep(2)#2-second delay
        
while True:#the while loop that repeats the code until the user decides to stop playing 
    choice = str.lower(input("rock paper scissors! ")) #saying rock paper scissors and it doesn't matter if you say it in lower case because of the str.lower

    if choice not in rps_options:
        print('only rock, paper, or scissors 5-second punishment delay')#if an answer is given that isn't rps then it print what is in quotes.
        time.sleep(5)#5 second delay
    else:
        bot_choice = (random.choice(rps_probabilities[rps_options.index(choice)]))#the bots choice is random from the list that is assigned to it
        print(bot_choice)# it prints the bots random choice from the list that is assigned to it        

        if choice == "rock": #if my peson says rock then it will print the list for the answer that is given
            if bot_choice == choice:#the botchoice equals a random choice from one of the list that are given
                print('we tied')#print this when both the bot and the person says rock
            elif bot_choice == 'paper': #if the bot says paper and the person says scissors then its prints whats below
                print('I win')#print this when the bot says scissors the person says paper
            elif botchoice == 'scissors':# #if the bot says scissors and the person says rock then its prints whats below
                print(' I lose')#print this when the bot says scissors the person says rock
        elif choice == "paper": #if my person says paper then it will print the list for the answer that is given
            if bot_choice == choice:#it prints the bots random choice from the list that is assigned to it      
                print('tie')#print this when both the bot and the person says paper
            elif botchoice == 'rock': #if the bot says rock and the person says paper then its prints whats below
                print('I lose')#print this when the bot says rock the person says paper
            elif bot_choice == 'scissors': #if the bot says scissors and the person says paper then its prints whats below
                print('I win') #print this when the bot says scissors the person says paper
        elif choice == "scissors": #if my person says scissors then it will print the list for the answer that is given
            if bot_choice == choice: #it prints the bots random choice from the list that is assigned to it      
                print('we tied') #print this when the bot says paper and the person says scissors
            elif bot_choice == 'rock': #if the bot says rock and the person say scissors then it prints whats below
                print('I win')#print this when the bot says rock the person says scissors
            elif bot_choice == 'paper': #if the bot says scissors and the person says scissors then its prints whats below
                print('I loss')#print this when both the bot and person says scissors

        time.sleep(0.5)#(0.5)second delay


        
     





