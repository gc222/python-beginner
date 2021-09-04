import random
from words import words
import string

# 1. First get a word to guess
# function to get a valid word from word.py

# 2. keep track of letters guessed/used 
    # we use a set because elements must be unique, so once used, it is accounted for
# 3. keep track of letters correctly guessed
    # we do this by condition, if is valid letter and is in word --> remove letter from word

# notice the reason for using a set. Storing the word in a set means that a word with
# multiple same letters is stored only once. 

# 4. Need a while loop until word is guessed i.e. word_letters.length() is 0

# 5. let user know what letters have been used

# 6. show user what letters is correct and use dashes for letters that haven't been guessed

# 7. add lives to the game

def get_valid_word(words):
    word = random.choice(words)     # randomly choose an element first
    # must choose a word that has no dashes or spaces within the word
    # while "-" in word or " " in word:   
    #     word = random.choice(words)
    
    if "-" or " " in word:
        word = random.choice(words)

    return word.upper()

    

def hangman():
    word = get_valid_word(words)    # get a valid word with words list as param

    
    # keep track using a set to store the letters of the word as individual elements
    word_letters = set(word)        # set("gregory") --> {'g', 'o', 'r', 'y', 'e'} 

    # store all uppercase alphabet letters as a set --> {'G', 'F', 'Q', 'W', ...}
    alphabet = set(string.ascii_uppercase)

    used_letters = set()    # what the user has guessed

    lives = 7

    # loops until word is guessed or when lives is 0
    while len(word_letters) > 0 and lives > 0:
        # print letters that have been used
        print("\n-----------------------------------------\n")
        print("You have ", lives, " lives and you have used these letters: ", ' '.join(used_letters))

        # iterate over the word: if letter is in used_letters return the letter
        # i.e. if letter is either a new letter (which has been added to used_letters) or has already been used, it will be printed
        # else: returns '_' for each letter in the word set i.e. _ _ _ _ _ 
        word_list = [letter if letter in used_letters else '_' for letter in word]              # used_letters = {}     word_list = ['e', ']
        print('The word is: \n', ' '.join(word_list))


        user_letter = input("Guess a letter: ").upper()
        # if user input is in the alphabet minus the used_letters i.e. an unused valid letter
        if user_letter in alphabet - used_letters:      
            used_letters.add(user_letter)           # record used letters
            # if it is in the word, remove the letter from the word_letters set
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:                       # else: not in word, take away a life
                lives -= 1
                print("Letter is not in word.")
        
        elif user_letter in used_letters:
            print("You have already used that letter. Please guess again.")

        else:
            print("Invalid character. Please guess again.")
    
    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print("You died, sorry. The word was:", word)
    else:
        print(f"You guessed the word: {word}!" )
    

hangman()









