import random# tells the code that their is a the random library
print('hello')
main = ["steak","spaghetti", "lobster","Cheeseburger","pasta","lobster","chicken"] # main course list one of the two lists for the parallel array and the first list that gets inserted 
side = ["with steamed vegetables"," with sauce", "with oysters", "with fries","with salad", "with eggplant","with rice"]# sides the second list that is inserted and is the second list for the parallel array 

dishes_amount = int(input('how many dishes would you like to order?'))# asking the user how many dishes they would like 

for i in range(dishes_amount):# repeats the amount of dishes until the number that was given was satisfied.
    print(f'''{random.choice(main)} {random.choice(side)}
    ''')# first picks a random choice from the list 'main' (the main courses) and then picks a random choice from the list 'side' (side courses) and then prints 
