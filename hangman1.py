import random

def choose_word():
    word_list = ['python','java','javascript','hangman','programming','developer','algorithm']
    return random.choice(word_list)

def display_word(word,guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display+=letter
        else:
            display+= "_"
    return display

def hangman():
    word=choose_word()
    guessed_letters=[]
    attempts = 6  
    guessed_word=False

    print("Welcome to Hangman!")
    print("Try to guess the word!")
    
    while attempts > 0 and not guessed_word:
        print("\nWord: " + display_word(word, guessed_letters))
        print(f"Remaining attempts: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Amazing Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Oops! '{guess}' is not in the word please checked it.")
        
        # Check if the whole word is guessed
        if all(letter in guessed_letters for letter in word):
            guessed_word = True

    if guessed_word:
        print("\nCongratulations, you guessed the word!")
    else:
        print(f"\nGame Over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
