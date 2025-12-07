#!/Users/ironic/mitpython/bin/python

# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


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

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    count = len(secret_word)
    for letter in letters_guessed:
        count -= secret_word.count(letter)
    if count == 0:
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    placeholder = '_ '
    retval = []

    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            retval.append(secret_word[i])
        else:
            retval.append(placeholder)

    return ''.join(retval)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alpha = list(string.ascii_lowercase)

    if len(letters_guessed) > 0:
        for letter in letters_guessed:
            alpha.remove(letter)

    return ''.join(alpha)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    unique_letters = 0
    vowels = 'aeiou'

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('--------')
    print('you have', warnings_remaining, 'warnings left.')

    while is_word_guessed(secret_word, letters_guessed) is not True and guesses_remaining > 0:
        print('you have %d guesses left.' % (guesses_remaining))
        print('Available letters:', get_available_letters(letters_guessed))

        letter = input('Please guess a letter: ').lower()

        # invalid entry: previously guessed letter or non-alpha character or more than 1 letter
        # lose a warning, or a guess if no more warnings left
        if letter in letters_guessed or letter.isalpha() is False or len(letter) != 1:
            warning = 'Oops! You already guessed that letter or you made an invalid entry. You have '
            if warnings_remaining > -1:
                warnings_remaining -= 1
                warning += str(warnings_remaining) + ' warnings left: '
            else:
                guesses_remaining -= 1
                warning += ' no warnings left so you lose a guess: '

            warning += get_guessed_word(secret_word, letters_guessed)
            print(warning)

        # valid entry
        else:
            letters_guessed.append(letter)
            if letter in secret_word:
                unique_letters += 1
                print('Good guess:', get_guessed_word(secret_word, letters_guessed))
            else:
                if letter in vowels:
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
                print('Oops! that letter is not in my word:', get_guessed_word(secret_word, letters_guessed))

        print('--------')

    if is_word_guessed(secret_word, letters_guessed):
        print('Congratulations, you won!')
        print('Your total score for this game is:', guesses_remaining * unique_letters)
    else:
        print('Sorry you ran out of guesses. The word was', secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    tmp = my_word.replace(' ', '')

    if len(tmp) != len(other_word):
        return False

    used_letters = []
    for letter in tmp:
        if letter.isalpha() and letter not in used_letters:
            used_letters.append(letter)

    # possible matching word if the for loop completes
    for i in range(len(tmp)):
        if tmp[i].isalpha():
            if tmp[i] != other_word[i]:
                return False
        # must be a '_ ' so return false if we've already compared this letter
        elif other_word[i] in used_letters:
            return False

    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matches = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            matches.append(other_word)
    if len(matches) > 0:
        print(matches)
    else:
        print('No matches found')

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    unique_letters = 0
    vowels = 'aeiou'

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('--------')
    print('you have', warnings_remaining, 'warnings left.')

    while is_word_guessed(secret_word, letters_guessed) is not True and guesses_remaining > 0:
        print('you have %d guesses left.' % (guesses_remaining))
        print('Available letters:', get_available_letters(letters_guessed))

        letter = input('Please guess a letter: ').lower()

        # invalid entry: previously guessed letter or non-alpha character or more than 1 letter
        # lose a warning, or a guess if no more warnings left
        if letter in letters_guessed or letter.isalpha() is False or len(letter) != 1:
            # user enters '*' for a hint
            if letter == '*':
                show_possible_matches(secret_word)
            else:
                warning = 'Oops! You already guessed that letter or you made an invalid entry. You have '
                if warnings_remaining > -1:
                    warnings_remaining -= 1
                    warning += str(warnings_remaining) + ' warnings left: '
                else:
                    guesses_remaining -= 1
                    warning += ' no warnings left so you lose a guess: '

                warning += get_guessed_word(secret_word, letters_guessed)
                print(warning)

        # valid entry
        else:
            letters_guessed.append(letter)
            if letter in secret_word:
                unique_letters += 1
                print('Good guess:', get_guessed_word(secret_word, letters_guessed))
            else:
                if letter in vowels:
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
                print('Oops! that letter is not in my word:', get_guessed_word(secret_word, letters_guessed))

        print('--------')

    if is_word_guessed(secret_word, letters_guessed):
        print('Congratulations, you won!')
        print('Your total score for this game is:', guesses_remaining * unique_letters)
    else:
        print('Sorry you ran out of guesses. The word was', secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
