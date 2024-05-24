import random#brings in the random library for the use of random functions
#the visual pictures for the hangman 
HANGMAN_PICS = ['''
     +---+
         |
        |
         |
        ===''', '''
     +---+
     O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

words = ("sesquipedalian","supercalifragilisticexpialidocious","worcestershire","onomatopoeia","malapropism",)#the random words that can be givenfor the user to guess
secret = random.choice(words)

secret_list = list(secret)
hidden = []
guesses = 0

for character in secret_list:
    hidden.append("_ ")
    
print("".join(hidden))

while "_ " in hidden and guesses < len(HANGMAN_PICS):
    print(HANGMAN_PICS[guesses])
    while True:
        guess = input("Enter a letter: ")

        if len(guess) != 1:
            print("enter a letter please!")
        else:
            break
    if guess in secret_list:
        for index in range(len(secret_list)):
            if guess == secret_list[index]:
                hidden[index] = guess
        print("".join(hidden))
    else:
        print("Letter not here!")
        guesses += 1


    
