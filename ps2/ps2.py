'''
2026.10.13
'''

import string
import random

WORDLIST_FILENAME = "words.txt"

# copy from the source
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word_guessed(secret_word,letters_guessed):
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word,letters_guessed):
    list = ""
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            list += '_'
        else:
            list += secret_word[i]
    return list

def get_available_letters(letters_guessed):
    list = string.ascii_lowercase
    for i in range(len(list)):
        if string.ascii_lowercase[i] in letters_guessed:
            list = list.replace(string.ascii_lowercase[i],"")
    return list

def hangman(secret_word,letters_guessed):
    pass
    

#print(is_word_guessed(secret_word,letters_guessed))
#print(get_guessed_word(secret_word,letters_guessed))
#print(get_available_letters(letters_guessed))
    
if __name__ == "__main__":
    letters_guessed = []
    left_time = 6
    warning_time = 3
    wordlist = load_words()
    #secret_word = random.choice(wordlist)
    secret_word = "bana"
    print("Welcome to the game Hangman! \n I am thinking of a word that is ",len(secret_word)," letters long. \n You have ",warning_time," warnings left. \n ------------- ")
    print("\nYou have ",left_time," guesses left. \n Available letters: ", get_available_letters(letters_guessed))
    i=0
    while True:
        letters_guessed.append(input("Please guess a letter:"))
        i+=1
        if not is_word_guessed(secret_word,letters_guessed):
            print("Good guess:",get_guessed_word(secret_word,letters_guessed))
        else:
            print("Oops! That letter is not in my word. ")
            
# This code was failed
# When I come back, finding I cannot understand it and I was frustrated
# so I build a new file. Please turn to "ps2_completed.py"