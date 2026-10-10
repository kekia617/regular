def is_word_guessed(secret_word, letters_guessed):

    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            return False

    return True

def get_guessed_word(secret_word, letters_guessed):
    result = ''

    for letter in secret_word:
        if letter not in letters_guessed:
            letter = '_'

        result += letter

    return result


def get_available_letters(letters_guessed):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for letter in letters:
        if letter in letters_guessed:
            continue
        result += letter
        
    return result

def hangman(secret_word='apple'):
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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    available_letters = alphabet
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3
    anwser = get_guessed_word(secret_word, letters_guessed)
    print(anwser)
    print('Welcome to the game Hangman!')
    print(f'You have {warnings_remaining} warnings left')
    print(f'I am thinking of a word that is {len(secret_word)} long.\n-------------')
    print(f'You have {guesses_remaining} guesses left.')
    print(f'Available letters: {available_letters}]')
    while anwser != secret_word and guesses_remaining > 0:
        letter = input('Please guess a letter: ').lower()
        if is_word_guessed(letter, alphabet):
            if is_word_guessed(letter, letters_guessed):
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    print(f"Oops! you've already guessed that letter. You have {warnings_remaining} warnings left:")
                    print(get_guessed_word(secret_word, letters_guessed))
                else:
                    guesses_remaining -= 1
                    print(f"Oops! You've already guessed that letter. You have no warnings left")
                    print(f"So you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                letters_guessed.append(letter)
                valid_letter = True
        else:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left")
                print(get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print(f"Oops! You've already guessed that letter. You have no warnings left")
                print(f"So you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")

        if valid_letter == True:
            if letter in secret_word:
                print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
                anwser = get_guessed_word(secret_word, letters_guessed)
            else:
                if letter == 'a' or letter =='e' or letter == 'i' or letter == 'o':
                    guesses_remaining -=  2
                    print(f"Please guess a letter: {anwser}")
                else:
                    guesses_remaining -= 1
                    print(f"Please guess a letter: {anwser}")

        print(guesses_remaining)
        valid_letter = False



def match_with_gaps(anwser, word):
    print(len(anwser), len(word))
    word = word.strip()
    i = 0
    if len(anwser) == len(word):
        for letter in anwser:
            if letter != '_':
                if letter != word[i]:
                    return False
            i += 1
    else:
        return False
    return True

def get_single_word(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    new_word = ''
    for letter in word:
        if letter in letters:
            new_word += letter

    return new_word

def show_possible_matches(wordlist, anwser):
    all_possible_words = ''
    new_word = ''
    for word in wordlist.split():
        new_word = get_single_word(word)
        if match_with_gaps(anwser, new_word):
            all_possible_words = all_possible_words + new_word + ' '

    print(all_possible_words)
