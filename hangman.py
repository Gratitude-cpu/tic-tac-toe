from random import choice, randomn

import random

#  programming author: Manusri Allam
# date: 11/23/2023
'''
# file: hangman.py is a program that users can play the game hangman by trying to guess the word 
the computer gives. There are restricted number of lives and certain word size
'''
# input: Inputs that are given by the user are word size and #of lives initially and then letters to guess the word, user chooses whether to restart the game
# output: Output the number of lives, whether the letter is correct or incorrect, restarts the game if user wants that

#Initial print statements
print("Welcome to the Hangman Game!")
#making dictionary from the dictionary of words
i = 0
while i <1:
    filename = "dictionary.txt"
    def import_dictionary(filename):
        f = open(filename, "r")
        d = {}
        for i in (f):
            word = i.strip()
            if len(word) in d:
                d[len(word)].append(word)
            elif (len(word) > 12):
                d[12].append(word)
            else:
                d[len(word)] = [word]
        return(d)
    #print(d)

    def get_game_options():
        word_size1 = 0
        lives1 = 0
        return(word_size1,lives1)

    #choosing word size from the user
    word_size = get_game_options()[0]
    lives = get_game_options()[1]
    try:
        word_size = int(input("Please choose a size of a word to be guessed [3 - 12, default any size]:\n"))
        if word_size < 3 or word_size > 12:
            print("A dictionary word of any size will be chosen.")
            word_size = random.choice([3,4,5,6,7,8,9,10,11,12])
        else:
            print(f'The word is set to {word_size}.')
    except:
        print("A dictionary word of any size will be chosen.")
        word_size = random.choice([3,4,5,6,7,8,9,10,11,12])
    #print(f'The word is set to {word_size}.')
    secret_word = choice(import_dictionary(filename)[word_size])
    #print(secret_word)

    #set lives 
    try:
        lives = int(input("Please choose a number of lives [1 – 10], default 5:\n"))
        if lives not in [1,2,3,4,5,6,7,8,9,10]:
            lives = 5
    except:
        lives = 5


    print(f'You have {lives} lives.')
    print("Letters chosen:")


    #underscores for the word size
    x = []
    for i in range(word_size):
        x.append('_')

    #Remembering the hyphen
    for i in secret_word:
        if i == "-":
            index1 =secret_word.index(i)
            x[index1] = "-"


    #O's for the lives size
    y = []
    i = 0
    while i < (lives):
        i = i+1
        y.append('O')


    letters_guessed = []

    print(" ".join(x) + "  " + (f' lives: {lives} ') + "".join(y))

    wrong_letters =  0

    while (lives > 0):
        guess = input("Please choose a new letter >\n")
        if guess in letters_guessed:
            print("You have already chosen this letter.")
            continue
        if guess in secret_word:
            print("You guessed right!")
        elif lives == 0:
            print(f'You lost! The word is {secret_word}!')
        else:
            lives -= 1
            wrong_letters +=1
            print("You guessed wrong, you lost one life.")
            #Hang life  from 0 --> x
        
        for i in range((wrong_letters)):
            y[i] = "X"


        #Maintain list of guessed letters
        
        
        letters_guessed.append(guess)

        
        print("Letters Chosen: " + ", ".join(letters_guessed))

        #boooks
    #    x = list(ui) #list of underscores for the size of the word
        #hangman user_interface
        for letter in secret_word:
            if letter in letters_guessed:
                s = secret_word.index(letter)
                x[s] = letter
                #print(x)
                for i in range (secret_word.count(letter)-1):
                    next_occr = (secret_word.index(letter,s+1))
                    x[next_occr] = letter
                    #print(x)
                    s = next_occr
        final_output = " ".join(x) + '  ' + (f' lives:  {lives} ') + "".join(y)
        print(final_output)

        if "".join(x) == secret_word:
            print(f'Congratulations!!! You won! The word is {secret_word}!')
            break
    if lives == 0:
        print(f"You lost! The word is {secret_word}!")

    cat = input('Would you like to play again [Y/N]? ')
    if cat == 'Y' or cat == 'y':
        i = 0
    else: 
        print("Goodbye!")
        i = i+1
        


                

                
        
                

                

                
                    
        
    




            

