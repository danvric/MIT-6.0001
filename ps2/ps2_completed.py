# 2026.10.20

import string
import random

WORDLIST_FILENAME = "words.txt"


# ============================================================
# copy from source
# ============================================================
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


# load
wordlist = load_words()


# ============================================================
# Problem 2: 3 helper function
# ============================================================
def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    result = ""
    for letter in secret_word:
        if letter in letters_guessed:
            result += letter
        else:
            result += "_ "
    return result


def get_available_letters(letters_guessed):
    available = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available += letter
    return available


# ============================================================
# Problem 4: Hint Helper
# ============================================================
def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(" ", "")

    if len(my_word) != len(other_word):
        return False

    for i in range(len(my_word)):
        if my_word[i] != "_":
            if my_word[i] != other_word[i]:
                return False
        else:
            if other_word[i] in my_word:
                return False

    return True


def show_possible_matches(my_word):
    matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matches.append(word)

    if matches:
        print(" ".join(matches))
    else:
        print("No matches found")


# ============================================================
# Problem 3 & 4: main
# ============================================================
def _play_hangman(secret_word, allow_hints):
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3
    vowels = "aeiou"

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings_remaining, "warnings left.")
    print("-------------")

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("You have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))

        guess = input("Please guess a letter: ").lower()
        
        if allow_hints and guess == "*":
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            continue

        if len(guess) != 1 or not guess.isalpha():
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter. You have",
                      warnings_remaining, "warnings left:",
                      get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            continue

        if guess in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter. You have",
                      warnings_remaining, "warnings left:",
                      get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            continue

        letters_guessed.append(guess)

        if guess in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            if guess in vowels:
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            print("Oops! That letter is not in my word:",
                  get_guessed_word(secret_word, letters_guessed))

        print("-------------")

    if is_word_guessed(secret_word, letters_guessed):
        score = guesses_remaining * len(set(secret_word))
        print("Congratulations, you won!")
        print("Your total score for this game is:", score)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word + ".")


def hangman(secret_word):
    _play_hangman(secret_word, allow_hints=False)


def hangman_with_hints(secret_word):
    _play_hangman(secret_word, allow_hints=True)


# ============================================================
# run
# ============================================================
if __name__ == "__main__":
    #secret_word = "tact"
    #hangman(secret_word)

    secret_word = random.choice(wordlist)
    hangman_with_hints(secret_word)