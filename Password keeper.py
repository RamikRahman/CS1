'''
Authors: Rami Rahman
Date: 5/13/24
Description: In this project you ask the user to asks their website, username, password and
the code stores the informaiton. the user after giving this information  will be able to acess their websites with their passwords and usernames if they choose to
until the user wants to stop. you can also enter as many websites you want.
bugs: nothing yet
challenges: adding function to my code and letting the user acess a specific website
with their username and passwords.
sources: w3schools ms marciono
'''

websites =  []                                                          # a list the user can put their websites in
usernames = []                                                          # a list the user can put their usernames in
passwords = []                                                          # a list the user can put their passwords in
def repeat():
      '''
      prints the website first then the line under is the usernames and lastly passwords

      Args:
            The usernames, passwords, and usernames that are given

      Returns:
            Their websites, passwords, and usernames that they give

      Raises:
            
      

      '''

                                                                        # function that makes the code more neat instead of repeating the code mutiple times
      print(f'''\nwebsites: {websites[i]}
        usernames:  {usernames[i]}
        passwords: {passwords[i]}''')                                   # this print the websites, usernames, and passwords in the order its meant to be in

while True:                                                             # repeats the code until the user choses to stop
    website = input("enter website ")                                   # asks for a website from the user
    username = input("enter username ")                                 # asks for a username from the user 
    password = input("enter password ")                                 # asks for a password from the user
    websites.append(website)                                            # adds the websites to the list that the user gives 
    usernames.append(username)                                          # adds the username to the list that the user gives
    passwords.append(password)                                          # adds the password to the list that the user gives
    
    access = input("pick a option: 1. print all, 2. print specific")    # asking the user if they want to print all of their website or a specific website they madr
    if access == '1':                                                   # if the user picks 1 then:
        for i in range(len(usernames)):                                 # the code will print all of the websites
           repeat()                                                     # the function
    elif access == "2":                                                 # if the user picks 2 then:
        name = input("enter a website")                                 # it will asks for a specific website

        if name in websites:                                            # if the name is in the websites then:
            i = websites.index(name)                                    # the code looks for the website names 
            repeat()                                                    # and print the information for the website
    end = input("do you want to end the code?")                         # asks the user if they want to end their code
    if end == 'yes':                                                    # if the user says end then it will end 
        break                                                           # ends the code if the if statement is given the correct answer the code will repeat itself
         