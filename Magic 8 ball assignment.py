import random

a = ['fantastic!!!', 'why', 'stop it!', 'goaway']


while True:
    eightball = input()
    if eightball == ("?"):
        break
   
 
        
    print(random.choice(a))


        
