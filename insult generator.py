import random# tells the code that the import file is in the code
print('hey there you')# asks a quesiton if someone if there 

mean = ["you stink!","your ugly","your dumb",] # the first thing that is said when someone asks for a insult
meaner = ["like a naked cat", " like a stinky bird"," and have big eyes"] # the second thing that prints when someone asks for a insult

insult_amount = int(input("how many times would you like to be insulted"))#asks the questions how many insult the user wants
for i in range(insult_amount):#
    print(f''' {random.choice(mean)} {random.choice(meaner)} 
    ''')# 

    
