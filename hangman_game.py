import random
import time

hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\  |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\  |
    /    |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\  |
    / \  |
         |
    ========="""
]

words = [ "python", "programming", "flower", "masters degree",
         "Liverpool", "DataScience", "Freya", "Playstation"]

def choose_word():
    return random.choice(words)

def display_state(guessed_letters, word, wrong_guesses):
    print(hangman_stages[wrong_guesses])
    print("\nWord: "," ".join(l if l in guessed_letters else "l" for l in word))
    print("Guessed letters:", ", ".join(sorted(guessed_letters)) or "None")
    print(f"Wrong guesses left: {6 - wrong_guesses}\n")

def get_guesses(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed this letter! Try another one.")
        else:
            return guess
        
def play():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_worg_guesses = 6

    print("Welcome to hangman!")
    print("Let me think a word for you.")
    print("...")
    time.sleep(3)
    print(f"Okay, the word has {len(word)} lettern.\n")

    while wrong_guesses < max_worg_guesses:
        display_state(guessed_letters, word, wrong_guesses)

        guess = get_guesses(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"Nice guess! {guess} is in the word.")
            if all(l in guessed_letters for l in word):
                display_state(guessed_letters, word, wrong_guesses)
                print(f"Congratulation! You won! :) The word was {word}!")
                break
        else:
            wrong_guesses += 1
            print(f"Unfortunately you guessed wrong. :( {guess} is not in the word.")
            print(f"You have{max_worg_guesses - wrong_guesses} guesses left.")
    else:
        print(hangman_stages[max_worg_guesses])
        print(f"\nGame over! The word was {word}.")

    if input("\nDo you want to play again? (y/n): ").lower() == "y":
        play()
    
if __name__ == "__main__":
    play()
