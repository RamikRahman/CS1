"""
Authors: Rami Rahman
Date: 11/6/2023
Description: This project is about my morning routine and what I do. It gives
basic yes or no questions to things that happen to me in the morning. This routine
starts when I am in the morning to when school starts.
bugs: you can type whenever you want
challenges: delay the str.lower, and a while loop.
sources: w3schools ms marciono 
"""

import time

print("Alarm1") # prints the what is inside of the quotes 
time.sleep(2)#2 second break 
print("Alarm2")# prints the what is inside of the quotes 
time.sleep(2)#2 second break
print("Alarm3")# prints the what is inside of the quotes 
time.sleep(2)#2 second break 


while True:#a loop until a correct answer is given
    tired = str.lower(input("tired?")) # the question that i being asked 
    if tired == "yes": # telling me that if im tired i will set a 4th alarm 
         print("Alarm4!")#it will print a 4th alarm
         break#if I don't put this in then it will continue to say what is going to be printed 
    elif tired == "no": # if im not then I get up 
        print("Get up!") #if it is not then it will print 'get up'
        break #if I don't put this in then it will continue to say what is going to be printed 
    else:
        print("Invalid response only yes or no") #they can only anwser with yes or no 
time.sleep(2) # 2 second break 
while True: # a loop if there is 
    still_tired = str.lower (input(" still tired?")) # my input is still tired and it asks if im still tired 
#str.lower means if someone gives the right answer but its captilized then it will be correct with the str.lower 
    if still_tired == "yes": #answers yes to the question am I still tired 
        print("go to shower") #it says in the code go to the shower 
        time.sleep(3) # it gives a 3 second break 
        break #if I don't put this in then it will continue to say go to the shower
    elif still_tired == "no":# one of the answers you can give 
        print ("put clothes on bed then shower") # prints what is in quotes 
        time.sleep(3)# three second break 
        break #if I don't put this in then it will continue to say what is going to be printed 
while True: #it is a loop if someone gives a incorrect response 
    
    breakfast = str.lower(input("do you want eggs?")) #asks if someone wants eggs

    if breakfast == "yes": #if the answer is yes then it will print eat food
        print("eat food")# prints the what is inside of the quotes 
        time.sleep(2)# 2 second break before it says the next thing
        break #if I don't put this in then it will continue to say eat food 
    elif breakfast == "no":# one of the answers you can give to the answers
        print ("then your gonna have pancakes!")# prints the what is inside of the quotes 
        time.sleep(2)# 2 second break before it says the next thing
        break#if I don't put this in then it will continue to say then your gonna have pancakes 

while True: # its a loop so if someone gives a incorrect answer then it repeats the questions 
    floss = str.lower(input("should I floss?")) # prints the what is inside of the quotes then answer with a yes or no question 

    if floss == "yes": # after the question is asked respond with yes 
        print("floss you have time!")# prints the what is inside of the quotes 
        time.sleep(1)# 1 second break inbtween 
        break #if I don't put this in then it will continue to say go to the shower
    elif floss == "no": # has to answer with a no 
        print("then do it later!") # prints the what is inside of the quotes 
        time.sleep(1) # 1 second break inbtween 
        break #if I don't put this in then it will continue to say go to the shower

while True: #a loop that repeats until a correct answer is given  
    talk = str.lower(input("should I go find people to talk to?")) # prints the what is inside of the quotes then answer with a yes or no question

    if talk == "yes": # one of the anwser you can give to the input 
        print("go find them") # prints the what is inside of the quotes 
        time.sleep(4) # 4 second break 
        break #if I don't put this in then it will continue to say go to the shower
    elif talk =="no": # one of the answers you can give to the question 
        print("you better go in the corner then and be lonely") # prints the what is inside of the quotes 
        time.sleep(4)# 4 second break
        break #if I don't put this in then it will continue to say go to the shower
while True: # its a loop so if someone gives a incorrect answer then it repeats the questions. 
    bye = str.lower(input("should I go?")) #it will ask if i should go then someone will answer with yes or no 

    if bye == "yes": # one of the answers you can give to the question 
        print("well then see ya!")# prints the what is inside of the quotes 
        break #if I don't put this in then it will continue well then see ya 
    elif bye == "no": #one of the answer you can give 
        print("too bad the bell rung!") # prints the what is inside of the quotes 
        break #if I don't put this in then it will continue to bad the bell rung 
