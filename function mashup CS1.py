import random# tells the code that their is a random library 
def main():
      
def chorus():# the one of the 7 function names and tells the code under it what its going to do  
      print("happy birthday to you")#

def sing():# the one of the 7 function names and tells the code under it what its going to do  
     chorus()# printing whatever is in the function 'chorus'  
     chorus()# printing whatever is in the function 'chorus' 
     print("happy birthday dear user")# in the function 
     chorus()# printing whatever is in the function 'chorus' 
def add(num1, num2): # the one of the 7 function names and tells the code under it what its going to do  
     print(num1+num2)
    

def is_a_number (string):# the one of the 7 function names and tells the code under it what its going to do  
    if string.isnumeric():
        return True #if the string is numeric then its will say its true
    else:# another word for saying otherwise 
        return False  =# if the string is not numeric then it will say it is not false  
def list_make (comma):# the one of the 7 function names and tells the code under it what its going to do  
    for i in comma:# loops the code and if their is a comma afterwards then it will loop and run that specific code again
        print(i)
def element(my_list, check):# the one of the 7 function names and tells the code under it what its going to do  
    if check in my_list:
        return True# if the element is in the list then it will return true 
    else:# if the element is not in the list then it will print whats below
        return False# if the element is not in the list then it will print false
def range(first_number, second_number):# the one of the 7 function names and tells the code under it what its going to do  
    print(random.randrange(first_number, second_number))

def replace_function( word, old_letter, new_letter):# the one of the 7 function names and tells the code under it what its going to do  
      new_word = "" #an empy space that acts about world 
      for letter in word:# a loop that tells you 
            if letter == old_letter:
                  new_word += new_letter
            else:
                  new_word += letter

      return new_word 
    
            
while True:#loops the code again 
    action = input("pick an activity 1-7")
       
    if action == '1':
        string = input("enter a number")
        print(is_a_number)
    
    elif action == '2':
        comma = input("what is your list? seprate by commas").split (",")
        list_make(comma)

    elif action =='3':
     num1 = int(input("what is your first number?"))
     num2 = int(input("what is your second number?"))
     add(num1,num2)
    elif action =='5':
        sing()
    elif action =='4': 
      ask = input("enter a list seperate by commas")
      enter = input("enter a element")
      print(element(ask, enter))
    elif action =='6':
      first_number = int(input("enter one number"))
      second_number = int(input("enter another number that has a higher numeric value then your first number"))
      range(first_number, second_number)
    elif action =='7':
        word = input("what is your word?")
        new_letter = input("enter one letter")
        old_letter = input("enter replacement letter")
        print(replace_function(word, new_letter, old_letter))
main()
        
