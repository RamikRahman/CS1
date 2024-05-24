'''
Author Rami
date 12/1
description a code block that tells the asks the user if they want to play rock paper scissors. both answers tell tehm to play anyways and the code continues
until the player users says to stop. if someone says scissors they have a 50% chance to get the anwser rock 30% cahnce to get paper and 20% to get scissors 
bugs Not that I know of 
challenges while loop
sources w3schools oliver servedio 
'''

import random#enter the random library
import time#enter the time libary 

a = ['rock','rock','rock','rock','rock','paper','paper', 'paper', 'scissors', 'scissors'] #random list
b = ['paper','paper','paper','paper','paper','scissors','scissors','scissors','rock','rock'] #random list 2
c = ['scissors','scissors','scissors','scissors','scissors','rock','rock','rock','paper', 'paper']#random list 3



while True: #the while loop continues until the yes or no question is answered
    play = str.lower(input("do you want to play rock paper scissors?"))#question do you want to play rock paper scissors? and it doesn't matter if its in caps
    #or lowercased
    if play == "yes": #if the answer is yes then it will print yes
        print("lets play!")# if the answer is yes then it will print lets play
        time.sleep(2)#2 second delay
        break#makes a break so the code doesn't continue
    elif play == "no": #if the answer is no then it will print thats too bad we are gonna play anyways
        print("thats too bad we are gonna play anyways!") #if the answer is no then it will print  thats too bad we are gonna play anyways
        time.sleep(2)#2 second delay
        break # a break to make sure the code doesn't continue
    else:#statment if a differnt answer is given
        print("only yes or no!")# the answer that is given if their is a differnt answer 
        time.sleep(2)#2 second delay
        
while True:#the while loop that reapeats the code until the user decides to stop playing 
    choice = str.lower(input("rock paper scissors!")) #saying rock paper scissors and it doesn't matter if you say it in lower case because of the str.lower

    if choice == "rock": #if my peson says rock then it will print the list for the answer that is given
        botchoice = (random.choice(b))#the bots choice is random from the list that is assigned to it
        print(botchoice)# it prints the bots random choice from the list that is assigned to it        
        if botchoice == choice:#the botchoice equals a random choice from one of the list that are given
            print('we tied')#print this when both the bot and the person says rock
            time.sleep(0.5)#(0.5)second delay
        elif botchoice == 'paper': #if the bot says paper and the person says scissors then its prints whats below
            print('I win')#print this when the bot says scissors the person says paper
            time.sleep(0.5)#(0.5)second delay
        elif botchoice == 'scissors':# #if the bot says scissors and the person says rock then its prints whats below
            print(' I lose')#print this when the bot says scissors the person says rock
            time.sleep(0.5)#(0.5)second delay
    elif choice == "paper": #if my person says paper then it will print the list for the answer that is given
        botchoice = (random.choice(a))#the bots choice is random from the list that is assigned to it
        print(botchoice)# it prints the bots random choice from the list that is assigned to it         
        if botchoice == choice:#it prints the bots random choice from the list that is assigned to it      
            print('tie')#print this when both the bot and the person says paper
            time.sleep(0.5)#(0.5)second delay
        elif botchoice == 'rock': #if the bot says rock and the person says paper then its prints whats below
            print('I lose')#print this when the bot says rock the person says paper
            time.sleep(0.5)#(0.5)second delay
        elif botchoice == 'scissors': #if the bot says scissors and the person says paper then its prints whats below
            print('I win') #print this when the bot says scissors the person says paper
            time.sleep(0.5)#(0.5)second delay
    elif choice == "scissors": #if my person says scissors then it will print the list for the answer that is given
        botchoice = (random.choice(a))#the bots choice is random from the list that is assigned to it
        print(botchoice)# it prints the bots random choice from the list that is assigned to it        
        if botchoice == choice: #it prints the bots random choice from the list that is assigned to it      
            print('we tied') #print this when the bot says paper and the person says scissors
            time.sleep(0.5)#(0.5)second delay
        elif botchoice == 'rock': #if the bot says rock and the person says scissors then its prints whats below
            print('I win')#print this when the bot says rock the person says scissors
            time.sleep(0.5)#(0.5)second delay
        elif botchoice == 'paper': #if the bot says scissors and the person says scissors then its prints whats below
            print('I loss')#print this when both the bot and person says scissors
            time.sleep(0.5)#(0.5)second delay
    else:#statment if a different answer is given 
        print('only rock, paper, or scissors 5 second punishment delay')#if a answer is given that isnt rps then it print what is in quotes.
        time.sleep(5)#5 second delay       
     
